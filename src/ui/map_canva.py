import customtkinter
from PIL import Image, ImageTk
import tkinter as tk
import os


class MapCanva():

    def __init__(self, current_map_page_id, window, zone_data, width, height):
        self.current_map_page_id = current_map_page_id
        self.window = window
        self.zone_data = zone_data
        self.width = width
        self.height = height

        self.create_map_canva()
        self.add_base_image()
        self.retrive_zone_image()

    def create_map_canva(self):
        self.map_canva = customtkinter.CTkCanvas(
            self.window,
            bg='#001220',
            width=self.width * 3/4,
            height=self.height * 26/27)
        self.map_canva.pack(side='bottom', anchor='sw', fill='both', expand=1)

    def update_image(self, current_map_page_id):
        self.clear_map_canvas()
        self.current_map_page_id = current_map_page_id
        self.retrive_zone_image()

    def clear_map_canvas(self):
        self.map_canva.delete("all")

    def add_base_image(self):
        if self.current_map_page_id == 1:
            self.image = 'Marisong.png'
            title = 'Marisong'
            description = 'Description'
            self.zone_data.add_base_image_to_table(
                self.current_map_page_id, title, description, self.image)
        else:
            None

    def retrive_zone_image(self):
        self.zone_image_file_name = self.zone_data.load_image_from_table_to_map(
            self.current_map_page_id)

        current_directory = os.path.dirname(os.path.abspath(__file__))
        project_directory = os.path.join(current_directory, '..')
        image_path_relative = os.path.join(
            'assets', self.zone_image_file_name[0])
        image_path = os.path.join(project_directory, image_path_relative)

        image_width = int(self.width * 3/4)
        image_height = int(self.height * 26/27)

        self.zone_image = customtkinter.CTkImage(
            light_image=Image.open(image_path), size=(image_width, image_height))
        self.image_label = customtkinter.CTkLabel(
            self.map_canva, image=self.zone_image, text='')
        self.image_label.place(x=0, y=0)
