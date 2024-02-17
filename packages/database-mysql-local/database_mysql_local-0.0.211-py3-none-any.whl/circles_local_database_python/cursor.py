from typing import Any

from logger_local.LoggerLocal import Logger

from .constants import LOGGER_CONNECTOR_CODE_OBJECT

logger = Logger.create_logger(object=LOGGER_CONNECTOR_CODE_OBJECT)


class Cursor:
    def __init__(self, cursor) -> None:
        self.cursor = cursor

    # TODO: If environment <> prod1 and dvlp1 break down using 3rd party package and analyze the formatted_sql
    #  and call private method _validate_select_table_name(table_name)
    def execute(self, sql_statement: str, sql_parameters: tuple = None) -> None:
        # TODO: validate_select_table_name(table_name)
        object1 = {
            "sql_statement": sql_statement,
            "sql_parameters": str(sql_parameters)
        }
        logger.start(object=object1)
        if sql_parameters:
            quoted_parameters = [
                "'" + str(param) + "'" for param in sql_parameters]
            formatted_sql = sql_statement % tuple(quoted_parameters)
            sql_parameters_str = ", ".join(quoted_parameters)
        else:
            formatted_sql = sql_statement
            sql_parameters_str = "None"
        EXECUTE_METHOD_NAME = 'database-mysql-local-python-package cursor.py execute()'
        logger.info(EXECUTE_METHOD_NAME, object={
            "full_sql_query": formatted_sql,
            "sql_parameters": sql_parameters_str,
            "sql_statement": sql_statement
        })
        try:
            self.cursor.execute(sql_statement, sql_parameters)
        except Exception as exception:
            logger.error(
                EXECUTE_METHOD_NAME + ", sql_statement:" + sql_statement +
                ", sql_parameters:" + str(sql_parameters),
                object={"exception": exception})
            raise exception
        logger.end(EXECUTE_METHOD_NAME)

    def fetchall(self) -> Any:
        logger.start()
        result = self.cursor.fetchall()
        logger.end("End of fetchall", object={'result': str(result)})
        return result

    def fetchone(self) -> Any:
        logger.start()
        result = self.cursor.fetchone()
        logger.end()
        return result

    def description(self) -> Any:
        logger.start()
        result = self.cursor.description
        logger.end(object={"result": str(result)})
        return result

    def lastrowid(self) -> int:
        logger.start()
        result = self.cursor.lastrowid
        logger.end(object={"result": str(result)})
        return result

    def close(self) -> None:
        logger.start()
        self.cursor.close()
        logger.end()
