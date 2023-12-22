import sqlite3
import os
import time


class TestDataBase:

    __test__ = False

    def __init__(self):
        self.database_path()
        self.connect_to_data_database()
        self.clear_database()

    def database_path(self):

        print(os.getcwd())
        if os.getcwd().endswith('test_utility'):
            self.db_path = os.path.abspath(
                os.path.join(os.getcwd(), 'test_data.db'))
        else:
            self.db_path = os.path.abspath(os.path.join(
                os.getcwd(), 'src', 'tests', 'test_utility', 'test_data.db'))

        print(self.db_path)

    def connect_to_data_database(self):
        self.connection = sqlite3.connect(
            'test_data.db', check_same_thread=False)
        self.cursor = self.connection.cursor()

    def clear_database(self):
        self.cursor.execute('DROP TABLE IF EXISTS users')
        self.cursor.execute('DROP TABLE IF EXISTS zone_base_data')
        self.cursor.execute('DROP TABLE IF EXISTS map_page')

        self.create_users_table()
        self.create_zone_base_data_table()
        self.create_map_page_table()

    def create_users_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                admin INTEGER)''')

    def create_zone_base_data_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS zone_base_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                zone_title TEXT,
                zone_description TEXT,
                zone_image TEXT)''')

    def create_map_page_table(self):

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS map_page (
                map_id INTEGER,
                zone_id INTEGER
                )''')
