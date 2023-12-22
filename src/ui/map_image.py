import customtkinter
from PIL import Image, ImageTk
import tkinter as tk
import os
from ui.base_frame import BaseFrame


class MapImage(BaseFrame):
    """
    A class that creates a frame for map images and loads in the map image.

    Attributes:
    - current_map_page_id (int): The identifier for the current map page.
    - window (tk.Tk): The main Tkinter window.
    - zone_data: An object providing data related to zones.
    - ui_utility: An instance of the UiUtility class for UI-related utility functions.
    """

    def __init__(self, current_map_page_id, window, zone_data, ui_utility):
        """
        Initializes a new instance of the MapImage class.

        Parameters:
        - current_map_page_id (int): The identifier for the current map page.
        - window (tk.Tk): The main Tkinter window.
        - zone_data: An object providing data related to zones.
        - ui_utility: An instance of the UiUtility class for UI-related utility functions.
        """
        super().__init__()
        self.current_map_page_id = current_map_page_id
        self.window = window
        self.zone_data = zone_data
        self.ui_utility = ui_utility

        self.width, self.height = self.ui_utility.get_size_in_relation_to_window(
            75, 95.5)
        self.x, self.y = self.ui_utility.get_size_in_relation_to_window(0, 4)

        self.__create_map_image_frame()
        self.__retrive_zone_image()

    def __create_map_image_frame(self):
        """ Private method to create the frame for displaying the map image."""

        self.map_image_frame = customtkinter.CTkFrame(
            self.window,
            bg_color=self.dark_blue,
            width=self.width,
            height=self.height)
        self.map_image_frame.place(x=self.x, y=self.y)

    def __retrive_zone_image(self):
        """Private method to retrieve and display the map image."""

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
            self.map_image_frame, image=self.zone_image, text='')
        self.image_label.place(x=0, y=0)
