import customtkinter
from PIL import Image, ImageTk
import tkinter as tk


class MapBaseFrame():

    def __init__(self, view_id, window, zone_data, width, height):
        self.view_id = view_id
        self.window = window
        self.zone_data = zone_data
        self.width = width
        self.height = height

        self.create_new_map_frame()
        self.add_zone_image()
        self.retrive_zone_image()

    def create_new_map_frame(self):
        self.map_frame = customtkinter.CTkFrame(
            self.window,
            bg_color='#001220',
            fg_color='#001220',
            width=self.width * 3/4,
            height=self.height)
        self.map_frame.place(x=0, y=0)

    def add_zone_image(self):
        self.image = 'Marisong.png'
        self.zone_data.add_image_data_to_table(self.view_id, self.image)

    def retrive_zone_image(self):
        self.zone_image_file_name = self.zone_data.load_data_from_table_to_map(
            self.view_id)
        image_path = f'assets/{self.zone_image_file_name[0]}'

        image_width = (self.width * 3/4)
        image_height = self.height

        self.zone_image = customtkinter.CTkImage(
            light_image=Image.open(image_path), size=(image_width, image_height))
        self.image_label = customtkinter.CTkLabel(
            self.map_frame, image=self.zone_image, text='')
        self.image_label.place(x=0, y=0)
