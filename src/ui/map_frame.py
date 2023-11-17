import customtkinter
from ui.base_frame import BaseFrame

class MapFrame(BaseFrame):

    def __init__(self, window, width, height, switch_state):
        super().__init__()
        self.window = window
        self.width = width
        self.height = height
        self.switch_state = switch_state

        self.create_new_frame()

    def create_new_frame(self):
        self.frame = customtkinter.CTkFrame(self.window, bg_color = '#001220', fg_color = '#6B8E23', width = self.width, height = self.height)
        self.frame.place(x = 0, y = 0)