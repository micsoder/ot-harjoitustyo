import customtkinter
from ui.base_frame import BaseFrame
from database.create_tables import CreateTables
from logic.zone_data_handler import ZoneDataHandler

class DashboardBaseFrame(BaseFrame):

    def __init__(self, view_id, window, zone_data, width, height):
        super().__init__()
        self.view_id = view_id
        self.window = window
        self.zone_data = zone_data
        self.width = width 
        self.height = height
        
        self.background_dashboard_frame()
        self.title_entry()
        self.label()
        self.add_text_to_dashboard()
        self.save_text_button()
        self.load_data()

    def background_dashboard_frame(self):
        self.dashboard_frame = customtkinter.CTkFrame(
            self.window,
            bg_color='#001220',
            fg_color='#3b5f7a',
            width=self.width * 1/4,
            height=self.height
        )
        self.dashboard_frame.place(x=self.width * 3/4, y=0)

    def title_entry(self):
        self.title = customtkinter.CTkEntry(
            self.dashboard_frame,
            font=self.font1,
            text_color='#fff',
            fg_color='#3b5f7a',
            bg_color='#3b5f7a',
            border_color='#fff',
            border_width=2,
            placeholder_text='Title of mapview',
            placeholder_text_color='#a3a3a3',
            width=350,
            height=70
        )
        self.title.place(x=10, y=20)
    
    def label(self):
        self.desc_label = customtkinter.CTkLabel(
            self.dashboard_frame, 
            text="Description", 
            font=self.font2,
            text_color='#fff',
            bg_color='#3b5f7a'
        )
        self.desc_label.place(x = 10, y = 110)
    
    def add_text_to_dashboard(self):
        self.description = customtkinter.CTkTextbox(
            self.dashboard_frame, 
            font=self.font3,
            text_color='#fff',
            fg_color='#3b5f7a',
            bg_color='#3b5f7a',
            border_color='#fff',
            border_width=2,
            width = 350, 
            height = 300,
            wrap = 'word')     
        self.description.place(x=10, y=150) 
    
    def save_text_button(self):
        self.save_button = customtkinter.CTkButton(
            self.dashboard_frame,
            text='Save',
            command = self.save_data,
            font=self.font2,
            text_color='#fff',
            fg_color='#00965d',
            hover_color='#006e44',
            bg_color='#121111',
            cursor='hand2',
            corner_radius=5,
            width=50
        )
        self.save_button.place(x=10, y=760)
    
    def load_data(self):
        self.zone_data.load_data_from_table_to_dashboard(self.view_id, self.title, self.description)
    
    def save_data(self):
        self.zone_data.save_data_from_dashboard_to_table(self.view_id, self.title, self.description)




















