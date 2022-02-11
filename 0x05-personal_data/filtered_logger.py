#!/usr/bin/env python3
"""
filtered_logger
"""

from typing import List
import re
import logging
import mysql.connector
import os

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """init"""
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        filter values in incoming log records using filter_datum
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(rf"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message


def get_logger() -> logging.Logger:
    """
    returns a logging.Logger object.
    """
    log = logging.getLogger("user_data")
    log.setLevel(logging.INFO)
    log.propagate = False
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(RedactingFormatter(PII_FIELDS))
    log.addHandler(streamHandler)
    return log


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    returns a connector to the database
    """
    user = os.environ.get('PERSONAL_DATA_DB_USERNAME', None)
    password = os.environ.get('PERSONAL_DATA_DB_PASSWORD', None)
    host = os.environ.get('PERSONAL_DATA_DB_HOST', None)
    database = os.environ.get('PERSONAL_DATA_DB_NAME', None)

    return mysql.connector.connect(user=user,
                                   password=password,
                                   host=host,
                                   database=database)


def main():
    """
    obtain a database connection using get_db and retrieve all rows.
    """

    connecter = get_db()
    cursor = connecter.cursor()
    table = "users"
    q = ("SELECT * FROM %s")
    cursor.execute(q, table)

    logger = get_logger()

    data = []
    for row in cursor:
        inf = f"name={row[0]}; email={row[1]}; phone={row[2]}; " \
              f"ssn={row[3]}; password={row[4]}; ip={row[5]}; " \
              f"last_login={row[6]}; user_agent={row[7]};"
        data.append(inf)

    for i in data:
        logger.info(data)

    cursor.close()
    connecter.close()


if __name__ == "__main__":
    main()
