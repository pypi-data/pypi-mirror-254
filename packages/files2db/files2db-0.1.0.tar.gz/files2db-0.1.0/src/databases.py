from abc import ABC, abstractmethod
from contextlib import contextmanager

from polars import LazyFrame
from pymysql import connect, MySQLError
from pymysql.cursors import DictCursor


class DatabaseConnectorClass(ABC):
    @abstractmethod
    def connect(self):
        """
        Establish a connection to the database.
        """
        pass

    @abstractmethod
    def get_schema(self, table_name: str):
        """
        Retrieve the schema of a given table.

        table_name (str): Name of the table to retrieve the schema for.
        """
        pass

    @abstractmethod
    def insert_data(self, table_name: str, data: LazyFrame):
        """
        Insert data into a given table.

        table_name (str): Name of the table to insert data into.
        data (LazyFrame): Data to be inserted.
        """
        pass


class MySQLConnector(DatabaseConnectorClass):
    def __init__(self, host: str, port: int, user: str, password: str, database: str):
        """Initialize MySQL connection parameters.

        Args:
            host (str): URL or IP address representation of database host
            port (int): Port number to connect to the database
            user (str): Database username for authentication
            password (str): Database password for authentication
            database (str): Target database name to store data
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    @contextmanager
    def connect(self):
        """
        Context manager to establish and close the database connection.
        Yields a connection object.
        """
        connection = connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            cursorclass=DictCursor,
            autocommit=False,
        )
        try:
            yield connection
        finally:
            connection.close()

    def get_schema(self, table_name):
        """
        Retrieve the schema of a given table.
        table_name (str): Name of the table to retrieve the schema for.
        """
        with self.connect() as connection:
            with connection.cursor() as cursor:
                query = f"DESCRIBE {table_name};"
                cursor.execute(query)
                schema = cursor.fetchall()
                return schema

    def insert_data(self, table_name, data_df):
        """
        Insert data into a given table.
        table_name (str): Name of the table to insert data into.
        data_df (LazyFrame): LazyFrame which contains data to be inserted
        """
        with self.connect() as connection:
            with connection.cursor() as cursor:
                columns = ", ".join(data_df.columns)
                values = data_df.rows()
                placeholders = ", ".join(["%s"] * len(values[0]))
                query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                try:
                    cursor.executemany(query, values)
                    connection.commit()
                except MySQLError as err:
                    print(f"Failed to insert data: {err}")
