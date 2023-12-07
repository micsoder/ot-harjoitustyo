import os
import customtkinter 
from ui.ui_handler import UiHandler
from ui.ui_utility import UiUtility
from database.initialize_database import DataBase
from database.create_tables import CreateTables


class Main():

    def __init__(self):
        print('Current Working Directory:', os.getcwd())
        self.create_root_window()
        self.create_database_connection()
        self.create_all_tables()
        self.create_ui_utility()
        self.initialize_ui_view()
        self.window.mainloop()
    
    def create_root_window(self):
        self.window = customtkinter.CTk()
        self.window.title('Atlas')

        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        self.window.geometry(f"{self.screen_width}x{self.screen_height}+0+0")

        self.window.config(bg='#001220')
       

    def create_database_connection(self):
        self.database = DataBase()

    def create_all_tables(self):
        CreateTables(self.database)
    
    def create_ui_utility(self):
        self.ui_utility = UiUtility(self.screen_width, self.screen_height)

    def initialize_ui_view(self):
        UiHandler(self.window, self.database, self.ui_utility)
    
