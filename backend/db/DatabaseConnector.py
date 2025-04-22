import os
import mysql.connector
from mysql.connector import Error
from dataclasses import dataclass, field




@dataclass
class DatabaseConnector:

    @staticmethod
    def get_connection():
        host: str = os.getenv("DB_HOST")
        port: int = int(os.getenv("DB_PORT"))
        user: str = os.getenv("DB_USER")
        password: str = os.getenv("DB_PASSWORD")
        database: str = os.getenv("DB_NAME")

        try:
            connection = mysql.connector.connect(host=host, port=port, user=user, password=password, database=database)

            if connection.is_connected():
                print("Verbindung zur Datenbank erfolgreich!")
                return connection
        except Error as e:
            print(f'Error while connecting to MySQL: {e}')