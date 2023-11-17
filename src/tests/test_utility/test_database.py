import sqlite3
import os

class TestDataBase:

    __test__ = False

    def __init__(self):
        self.database_path()
        self.connect_to_data_database()

    def setup_method(self):
        self.clear_database()

    def teardown_method(self):
        self.connection.close()

    def database_path(self):
        self.db_path = os.path.join("test_data.db")

    def connect_to_data_database(self):
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def clear_database(self):
        self.cursor.execute('DROP TABLE IF EXISTS users')
        self.create_users_table()

    def create_users_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT NOT NULL,
                password TEXT NOT NULL)''')

