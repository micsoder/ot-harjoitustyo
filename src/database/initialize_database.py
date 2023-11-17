import sqlite3
import os

class DataBase():

    def __init__(self):
        print('Connecting to database...')
        self.database_path()
        self.connect_to_data_database()

    def database_path(self):
        if os.getcwd().endswith('src'):
            self.db_path = os.path.abspath(os.path.join(os.getcwd(), 'database', 'data.db'))
        else:
            self.db_path = os.path.abspath(os.path.join(os.getcwd(), 'src', 'database', 'data.db'))
        print(self.db_path)

    def connect_to_data_database(self):
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        print('Connection to database established.')

    
