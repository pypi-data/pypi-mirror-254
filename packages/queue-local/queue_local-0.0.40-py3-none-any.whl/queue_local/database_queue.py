import json
import os
from collections.abc import Iterable
from enum import Enum

import mysql.connector
from database_mysql_local.generic_crud import GenericCRUD
from logger_local.LoggerComponentEnum import LoggerComponentEnum
from logger_local.LoggerLocal import Logger
from user_context_remote.user_context import UserContext

from .our_queue import OurQueue

QUEUE_LOCAL_PYTHON_COMPONENT_ID = 155
QUEUE_LOCAL_PYTHON_COMPONENT_NAME = "queue_local/src/database_queue.py"
DEVELOPER_EMAIL = 'akiva.s@circ.zone'


class StatusEnum(Enum):
    NEW = 0
    RETRIEVED = 1


class DatabaseQueue(OurQueue, GenericCRUD):
    """A queue that uses a database table as the queue."""

    def __init__(self, schema_name: str = "queue", table_name: str = "queue_item_table",
                 view_name: str = "queue_item_view", id_column_name: str = "queue_item_id",
                 is_test_data: bool = False) -> None:
        """Initialize the queue.
        Make sure the table has the following columns:
            queue_status_id, action_id, process_id, user_jwt
            created_user_id, updated_user_id
            created_timestamp, updated_timestamp, start_timestamp, end_timestamp

        ALTER TABLE `invitation`.`invitation_table` 
            ADD COLUMN `queue_status_id` SMALLINT UNSIGNED NULL AFTER `updated_effective_profile_id`,
            ADD COLUMN `action_id` SMALLINT UNSIGNED NULL AFTER `queue_status_id`,
            ADD COLUMN `process_id` MEDIUMINT UNSIGNED NULL AFTER `action_id`,
            ADD COLUMN `user_jwt` VARCHAR(255) NULL AFTER `process_id`;


        Default schema_name = the first part of the table_name, before the first underscore.
        Default view_name = table_name with "_view" instead of "_table"
            (or "_view" added to the end if there is no "_table").
        You can pass a Connector object to use an existing connection, or None to create a new connection.
        """
        self.logger = Logger(
            object={
                'component_id': QUEUE_LOCAL_PYTHON_COMPONENT_ID,
                'component_name': QUEUE_LOCAL_PYTHON_COMPONENT_NAME,
                'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
                'developer_email': DEVELOPER_EMAIL
            }
        )
        if not view_name:
            if table_name.endswith("_table"):
                view_name = table_name.replace("_table", "_view")
            else:
                view_name = table_name + "_view"
        if not schema_name:
            schema_name = table_name.split("_")[0]
        self.id_column_name = id_column_name

        GenericCRUD.__init__(self, default_schema_name=schema_name, default_table_name=table_name,
                             default_view_table_name=view_name, default_id_column_name=id_column_name,
                             is_test_data=is_test_data)
        self.logger.info("DatabaseQueue initialized successfully", object={
            "schema_name": schema_name, "table_name": table_name,
            "view_name": view_name, "id_column_name": id_column_name})
        self.user_context = UserContext().login_using_user_identification_and_password()

    def push(self, data_json: dict) -> int:
        """Pushes a new entry to the queue.
        data_json consists of columns and values to insert into the queue table."""
        created_user_id = UserContext().get_effective_user_id()
        self.logger.start("Pushing entry to the queue database", object={"data_json": data_json})

        try:
            self._fix_parameters_json(data_json)

            data_json["queue_status_id"] = StatusEnum.NEW.value
            data_json["created_user_id"] = created_user_id

            queue_id = self.insert(data_json=data_json)  # returning the queue_id for messages-local
            self.logger.end("Entry pushed to the queue database successfully")
        except Exception as exception:
            self.logger.error("Error while pushing entry to the queue database", object=exception)
            raise exception
        return queue_id

    def push_back(self, queue_item: dict) -> None:
        """Push a taken queue item back to the queue."""
        self.logger.start("Pushing back queue item", object=queue_item)
        data_json = {"queue_status_id": StatusEnum.NEW.value, "process_id": None}
        self.update_by_id(id_column_value=queue_item[self.id_column_name], data_json=data_json)
        self.logger.end("Queue item pushed back successfully")

    def get(self, action_ids: tuple = ()) -> dict:
        """
        Returns the first item from the queue (possibly considering specific actions) and marks it as taken.

        :param action_ids: Tuple of action IDs to consider (optional).
        :return: Dictionary representing the retrieved queue item.
        """
        updated_user_id = self.user_context.get_effective_user_id()
        self.logger.start("Getting and updating queue item from the queue database", object={"action_ids": action_ids})
        action_ids = self._fix_action_ids(action_ids)

        try:
            data_json = {"process_id": os.getpid()}
            update_where = f"process_id IS NULL AND queue_status_id = {StatusEnum.NEW.value} AND " \
                           f"NOW() > start_timestamp AND (end_timestamp is NULL or NOW() < end_timestamp)" + \
                           (f" AND action_id IN {action_ids}" if action_ids else "")
            self.update_by_where(where=update_where, order_by="created_timestamp", limit=1, data_json=data_json)

            select_where = f"process_id = {os.getpid()} AND queue_status_id = {StatusEnum.NEW.value}"
            queue_item = self.select_one_dict_by_where(where=select_where)
            if queue_item:
                # Update the selected queue item
                query = f"UPDATE {self.schema_name}.{self.default_table_name} " \
                        f"SET queue_status_id=%s, updated_user_id=%s, user_jwt=%s, updated_timestamp = NOW() " \
                        f"WHERE {self.id_column_name} = %s"
                params = (StatusEnum.RETRIEVED.value, updated_user_id, self.user_context.get_user_jwt(),
                          queue_item[self.id_column_name])
                self.cursor.execute(query, params)
                self.connection.commit()
                self.logger.end("Entry retrieved and updated from the queue database successfully",
                                object=queue_item)
            else:
                self.logger.end("The queue is empty")
        except mysql.connector.Error as exception:
            self.connection.rollback()
            self.logger.error("Error while getting and updating queue item from the queue database",
                              object=exception)
            raise exception
        return queue_item

    def peek(self, action_ids: tuple = ()) -> dict:
        """Get the first item in the queue without changing it"""
        action_ids = self._fix_action_ids(action_ids)
        where = f"process_id IS NULL AND queue_status_id = {StatusEnum.NEW.value}" + \
                (f" AND action_id IN {action_ids}" if action_ids else "")
        try:
            self.logger.start("Peeking queue item from the queue database")
            queue_item = self.select_one_dict_by_where(where=where, order_by="created_timestamp")
            self.logger.end("Entry peeked from the queue database successfully" if queue_item else "The queue is empty")
        except Exception as e:
            self.logger.exception("Error while peeking queue item from the queue database", object=e)
            raise
        return queue_item

    def _fix_action_ids(self, action_ids):
        """Fixes the action_ids argument to fit the SQL syntax (action_id IN action_ids)"""
        if isinstance(action_ids, int):
            action_ids = (action_ids,)
        elif isinstance(action_ids, Iterable):
            action_ids = tuple(action_ids)
        else:
            self.logger.error("get_by_action_ids (queue database) invalid argument", object={"action_ids": action_ids})
            raise ValueError("`action_ids` must be a tuple")
        return action_ids if len(action_ids) != 1 else f"({action_ids[0]})"

    @staticmethod
    def _fix_parameters_json(data_json: dict):
        """Fixes the parameters_json argument to fit the SQL syntax (parameters_json must be a string)"""
        for key, value in data_json.items():
            if "parameters_json" in key:
                if isinstance(value, str):
                    data_json[key] = value.replace("'", '"')
                else:
                    data_json[key] = json.dumps(value)
