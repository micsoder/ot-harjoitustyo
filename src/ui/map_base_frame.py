import customtkinter

class MapBaseFrame():

    def __init__(self, view_id, window, map_data_handler, width, height):
        self.view_id = view_id
        self.window = window
        self.map_data_handler = map_data_handler
        self.width = width 
        self.height = height
        
        self.create_new_map_frame()

    def create_new_map_frame(self):
        self.map_frame = customtkinter.CTkFrame(
            self.window,
            bg_color='#001220',
            fg_color='#001220',
            width=self.width * 3/4,
            height=self.height)
        self.map_frame.place(x=0, y=0)
        # Add map-related components here