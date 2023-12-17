import customtkinter
from PIL import Image, ImageTk
import tkinter as tk
import os
from ui.base_frame import BaseFrame


class MapCanva(BaseFrame):

    def __init__(self, current_map_page_id, window, zone_data, ui_utility):
        super().__init__()
        self.current_map_page_id = current_map_page_id
        self.window = window
        self.zone_data = zone_data
        self.ui_utility = ui_utility

        self.width, self.height = self.ui_utility.get_size_in_relation_to_window(75, 96)
        self.x, self.y = self.ui_utility.get_size_in_relation_to_window(0, 4)

        self.create_map_canva()
        self.retrive_zone_image()

    def create_map_canva(self):
        self.map_canva = customtkinter.CTkFrame(
            self.window,
            bg_color=self.dark_blue,
            width=self.width,
            height=self.height)
        self.map_canva.place(x=self.x, y=self.y)

    def retrive_zone_image(self):
        self.zone_image_file_name = self.zone_data.load_image_from_table_to_map(
            self.current_map_page_id)

        current_directory = os.path.dirname(os.path.abspath(__file__))
        project_directory = os.path.join(current_directory, '..')
        image_path_relative = os.path.join(
            'assets', self.zone_image_file_name[0])
        image_path = os.path.join(project_directory, image_path_relative)

        image_width = int(self.width)
        image_height = int(self.height)

        self.zone_image = customtkinter.CTkImage(
            light_image=Image.open(image_path), size=(image_width, image_height))
        self.image_label = customtkinter.CTkLabel(
            self.map_canva, image=self.zone_image, text='')
        self.image_label.place(x=0, y=0)
