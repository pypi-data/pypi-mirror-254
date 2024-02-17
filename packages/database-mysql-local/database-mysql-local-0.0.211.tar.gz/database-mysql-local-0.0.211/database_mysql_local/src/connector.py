import mysql.connector
import python_sdk_remote.utilities as utilities
from logger_local.LoggerLocal import Logger

from .constants import LOGGER_CONNECTOR_CODE_OBJECT
from .cursor import Cursor

logger = Logger.create_logger(object=LOGGER_CONNECTOR_CODE_OBJECT)
connections_pool = {}


# TODO Can we add hostname, IPv4, IPv6, sql statement? Can we have the same message format in all cases?
class Connector:
    @staticmethod
    def connect(schema_name: str) -> 'Connector':
        logger.start(object={"schema_name": schema_name})
        if (schema_name in connections_pool and
                connections_pool[schema_name] and
                connections_pool[schema_name].connection):
            if connections_pool[schema_name].connection.is_connected():
                logger.end("Return existing connections_pool", object={
                    'connections_pool': str(connections_pool[schema_name])})
                return connections_pool[schema_name]
            else:
                # reconnect
                connections_pool[schema_name].connection.reconnect()
                # TODO We should develop retry mechanism to support password rotation and small network issues.
                if connections_pool[schema_name].connection.is_connected():
                    logger.end("Reconnected successfully", object={
                        'connections_pool': str(connections_pool[schema_name])})
                    return connections_pool[schema_name]
                else:
                    connector = Connector(schema_name)
                    logger.error("Reconnect failed, returning a new connection",
                                 object={'connections_pool': str(connections_pool[schema_name])})

                    return connector
        else:
            connector = Connector(schema_name)
            logger.end("Return connections_pool with a new connector",
                       object={'connector': str(connector)})
            return connector

    def __init__(self, schema_name: str,
                 host: str = utilities.get_sql_hostname(),
                 user: str = utilities.get_sql_username(),
                 password: str = utilities.get_sql_password()) -> None:
        logger.start(object={"schema_name": schema_name, "host": host, "user": user})
        required_args = (host, user, password)
        if not all(required_args):
            error_message = "Error: Please add RDS_HOSTNAME, RDS_USERNAME and RDS_PASSWORD to .env or GitHub Actions variables and secrets"
            logger.error(error_message)
            raise Exception(error_message)

        self.host = host
        self.schema = schema_name
        self.user = user
        self.password = password

        # Checking host suffix
        if not (self.host.endswith("circ.zone") or self.host.endswith("circlez.ai")):
            logger.error(
                f"Warning: Your RDS_HOSTNAME={self.host} which is not what is expected")
        self.connection: mysql.connector = None
        self._cursor = None
        self._connect_to_db()
        connections_pool[schema_name] = self
        logger.end()

    def reconnect(self):
        logger.start("connect Attempting to reconnect...")
        try:
            self.connection.reconnect()
            self._cursor = self.connection.cursor()
            self.set_schema(self.schema)
        except mysql.connector.Error as exception:
            logger.error(f"Couldn't connect to the database {self.database_info()}", object={"exception": exception})
            logger.end()
            raise exception
        logger.end(object={"self": str(self)})
        return self

    def _connect_to_db(self):
        logger.start("connect Attempting to connect...")
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.schema
            )
            self._cursor = self.connection.cursor()
            self.set_schema(self.schema)

        except mysql.connector.Error as exception:
            logger.error(f"Couldn't connect to the database {self}", object={"exception": exception})
            logger.end()
            raise exception
        logger.end(object={"self": str(self)})
        return self

    def database_info(self):
        return f"host={self.host}, user={self.user}, schema={self.schema}"

    def __str__(self):
        return self.database_info()

    def close(self) -> None:
        logger.start()
        try:
            if self._cursor:
                self._cursor.close()
                logger.info("Cursor closed successfully.")
        except Exception as exception:
            logger.error(f"connection.py close() {self.database_info()}", object={"exception": exception})

        try:
            if self.connection and self.connection.is_connected():
                self.connection.close()
                logger.info("Connection closed successfully.")
        except Exception as exception:
            logger.error(f"connection.py close() {self.database_info()}", object={"exception": exception})
            raise exception
        finally:
            logger.end()

    def cursor(self, dictionary=False, buffered=False) -> Cursor:
        logger.start("cursor asked", object={
            "dictionary": dictionary, "buffered": buffered})
        cursor_instance = Cursor(self.connection.cursor(
            dictionary=dictionary, buffered=buffered))
        logger.end("Cursor created successfully", object={
            "cursor_instance": str(cursor_instance)})
        return cursor_instance

    def commit(self) -> None:
        logger.start("commit to database")
        self.connection.commit()
        logger.end(object={})

    def set_schema(self, new_schema: str | None) -> None:
        if not new_schema:
            return
        logger.start(object={"new_schema": new_schema})
        if self.schema == new_schema:
            logger.end(f"Schema is already {new_schema}. No need to switch to it.")
            return
        self.schema = new_schema
        if self.connection and self.connection.is_connected():
            use_query = f"USE `{new_schema}`;"
            try:
                self._cursor.execute(use_query)
                logger.info(f"Switched to schema: {new_schema}")
            except mysql.connector.Error as exception:
                logger.error(f"sql_statement: {use_query} at {self.database_info()}", object={"exception": exception})
                logger.end()
                raise exception
        else:
            logger.error(
                "Connection is not established. The database will be used on the next connect.")
        logger.end()

    def rollback(self):
        logger.start()
        self.connection.rollback()
        logger.end()

    def start_tranaction(self):
        logger.start()
        self.connection.start_transaction()
        logger.end()
