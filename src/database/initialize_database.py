import sqlite3
import os


class DataBase():
    """A simple class to manage connections to an SQLite database."""
    def __init__(self):
        """
        Initializes a new instance of the DataBase class.
        This constructor connects to the SQLite database.
        """
        print('Connecting to database...')
        self.__database_path()
        self.__connect_to_data_database()

    def __database_path(self):
        """Private method to determine the correct path for the SQLite database file."""
        if os.getcwd().endswith('src'):
            self.db_path = os.path.abspath(
                os.path.join(os.getcwd(), 'database', 'data.db'))
        else:
            self.db_path = os.path.abspath(os.path.join(
                os.getcwd(), 'src', 'database', 'data.db'))
        print(self.db_path)

    def __connect_to_data_database(self):
        """Private method to establish a connection to the SQLite database."""
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        print('Connection to database established.')
