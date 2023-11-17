import sqlite3
import os


class DataBase():

    def __init__(self):
        print('Connecting to database...')
        self.database_path()
        self.connect_to_data_database()
    
    def database_path(self):
        self.script_path = os.path.abspath('./database/')
        self.db_path = os.path.join(os.path.dirname(self.script_path), "database\data.db")

    def connect_to_data_database(self):
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        print('Connection to database established...')

    
