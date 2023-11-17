from ui.signup_frame import SignupFrame
from ui.login_frame import LoginFrame
from ui.map_frame import MapFrame
import tkinter as tk
from logic.user_handler import UserHandler

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

        self.user_handler = UserHandler(self.database)

        self.switch_frame(0)
    
    def switch_frame(self, frame_id):
        if frame_id == 0:
            SignupFrame(self.window, self.font1, self.font2, self.font3, self.font4, self.user_handler, self.switch_frame)
        if frame_id == 1:
            LoginFrame(self.window, self.font1, self.font2, self.font3, self.font4, self.user_handler, self.switch_frame) 
        if frame_id == 2:
            MapFrame(self.window, self.screen_width, self.screen_height, self.switch_frame)













    

        
    

