from ui.create_signup_frame import SignupFrame
from ui.create_login_frame import LoginFrame
from ui.create_map_frame import MapFrame
import tkinter as tk

class UiHandler():

    def __init__(self, window, database):

        self.window = window
        self.database = database

        self.font1 = ('Helvetica', 25, 'bold')
        self.font2 = ('Arial', 17, 'bold')
        self.font3 = ('Arial', 13, 'bold')
        self.font4 = ('Arial', 13, 'bold', 'underline')

        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        self.create_signup_frame()

    def create_signup_frame(self):
        self.start = SignupFrame(self.window, self.font1, self.font2, self.font3, self.font4, self.database, self.create_login_frame)

    def create_login_frame(self):
        LoginFrame(self.window, self.font1, self.font2, self.font3, self.font4, self.database, self.create_map_frame) 
    
    def create_map_frame(self):
        MapFrame(self.window, self.screen_width, self.screen_height)

    

        
    

