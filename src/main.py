from ui.ui_handler import UiHandler
from database.initialize_database import DataBase
from database.create_tables import CreateTables

class Main():

    def __init__(self, window):
        self.window = window

        self.create_database_connection()
        self.create_user_table()
        self.initialize_ui_view()
        
    def create_database_connection(self):
        self.database = DataBase()
    
    def create_user_table(self):
        CreateTables(self.database)

    def initialize_ui_view(self):
        UiHandler(self.window, self.database)


