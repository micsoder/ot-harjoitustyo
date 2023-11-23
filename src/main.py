import os
from ui.ui_handler import UiHandler
from database.initialize_database import DataBase
from database.create_tables import CreateTables


class Main():

    def __init__(self, window):
        self.window = window
        print('Current Working Directory:', os.getcwd())
        self.create_database_connection()
        self.create_all_tables()
        self.initialize_ui_view()

    def create_database_connection(self):
        self.database = DataBase()

    def create_all_tables(self):
        CreateTables(self.database)

    def initialize_ui_view(self):
        UiHandler(self.window, self.database)
