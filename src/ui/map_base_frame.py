import customtkinter
from PIL import Image, ImageTk
import tkinter as tk
import os


class MapBaseFrame():

    def __init__(self, view_id, window, zone_data, width, height):
        self.view_id = view_id
        self.window = window
        self.zone_data = zone_data
        self.width = width
        self.height = height

        self.create_new_map_canva()
        self.add_zone_image()
        self.retrive_zone_image()

        self.rectangles = []

        self.window.bind("<Button-3>", self.show_optionmenu)

    def create_new_map_canva(self):
        self.map_canva = customtkinter.CTkCanvas(
            self.window,
            bg='#001220',
            width=self.width * 3/4,
            height=self.height)
        self.map_canva.pack(anchor='nw', fill = 'both', expand = 1)

    def add_zone_image(self):
        self.image = 'Marisong.png'
        self.zone_data.add_image_data_to_table(self.view_id, self.image)

    def retrive_zone_image(self):
        self.zone_image_file_name = self.zone_data.load_data_from_table_to_map(
            self.view_id)

        current_directory = os.path.dirname(os.path.abspath(__file__))
        project_directory = os.path.join(current_directory, '..')
        image_path_relative = os.path.join('assets', self.zone_image_file_name[0])
        image_path = os.path.join(project_directory, image_path_relative)

        #if os.getcwd().endswith('ot-harjoitustyo'):
            #image_path = f'src/assets/{self.zone_image_file_name[0]}'
            #print('Current Working Directory:', os.getcwd())

        #else:
            #image_path = f'assets/{self.zone_image_file_name[0]}'
            #print('Current Working Directory:', os.getcwd())

        image_width = int(self.width * 3/4)
        image_height = int(self.height)

        self.zone_image = customtkinter.CTkImage(
            light_image=Image.open(image_path), size=(image_width, image_height))
        self.image_label = customtkinter.CTkLabel(
            self.map_canva, image=self.zone_image, text='')
        self.image_label.place(x=0, y=0)

    def show_optionmenu(self, event):

        optionmenu_var = customtkinter.StringVar(value = 'Options')
        option_combobox = customtkinter.CTkOptionMenu(
            self.map_canva, 
            values = ['Add zone', 'Add NPC'],
            variable = optionmenu_var,
            command = self.optionmenu_callback)
    
        option_combobox.place(x = 10, y = 10)

    def optionmenu_callback(self, selection):
        if selection == 'Add zone':
            self.zone_information_frame()   
        else: 
            None
    
    def zone_information_frame(self):
        self.information_frame = customtkinter.CTkFrame(
            self.map_canva,
            bg_color = '#FFFFFF',
            fg_color = '#FFFFFF',
            width = 140,
            height = 140
        )

        self.information_frame.place(x = 10, y = 50)
        self.zone_information_label()
        self.zone_title_entry()
        self.zone_image_file_entry()
        self.mark_zone_button()
        self.save_button()

    def zone_information_label(self):
        self.zone_label = customtkinter.CTkLabel(
            self.information_frame,
            text = "Zone Information",
            text_color = 'black',
            bg_color = '#FFFFFF',
            fg_color = '#FFFFFF',
        )
        self.zone_label.place(x=10, y=5)
    
    def zone_title_entry(self):
        self.title = customtkinter.CTkEntry(
            self.information_frame,
            text_color='black',
            bg_color='#FFFFFF',
            fg_color='#E5F0DD',
            border_color='#E5F0DD',
            border_width=2,
            placeholder_text='Add title',
            placeholder_text_color='#a3a3a3',
            width=120,
            height=20
        )
        self.title.place(x=10, y=40)

    def zone_image_file_entry(self):
        self.image_entry = customtkinter.CTkEntry(
            self.information_frame,
            text_color='black',
            bg_color='#FFFFFF',
            fg_color='#E5F0DD',
            border_color='#E5F0DD',
            border_width=2,
            placeholder_text='Add image filename',
            placeholder_text_color='#a3a3a3',
            width=120,
            height=20
        )
        self.image_entry.place(x=10, y=70)

    def mark_zone_button(self):
        self.mark_zone_button = customtkinter.CTkButton(
            self.information_frame,
            text='Mark zone',
            command=self.mark_zone_rectangle,
            text_color='black',
            bg_color='#FFFFFF',
            fg_color='#6EA149',
            border_color='#6EA149',
            hover_color='#56793C',
            cursor='hand2',
            corner_radius=5,
            width=40
        )
        self.mark_zone_button.place(x=10, y=100)

    def save_button(self):
        self.save_button = customtkinter.CTkButton(
            self.information_frame,
            text='Save',
            command=self.save_zone_information,
            text_color='black',
            bg_color='#FFFFFF',
            fg_color='#6EA149',
            border_color='#6EA149',
            hover_color='#56793C',
            cursor='hand2',
            corner_radius=5,
            width=30
        )
        self.save_button.place(x=90, y=100)

    def mark_zone_rectangle(self):
        self.window.bind("<Button-1>", self.get_x_and_y)
        self.window.bind("<B1-Motion>", self.draw_rectangle)
    
    def get_x_and_y(self, event):
        self.lasx, self.lasy = event.x, event.y
    
    def draw_rectangle(self, event):

        x, y = self.lasx, self.lasy
        width, height = event.x - x, event.y - y
        print(f'Rectangle coordinates: x={x}, y={y}, width={width}, height={height}')  
        rect_id = self.map_canva.create_rectangle(x, y, event.x, event.y, outline='red', width=2, fill='', tags='rectangle')

        # Save the rectangle coordinates in the list
        self.rectangles.append({
            'id': rect_id,
            'coordinates': (x, y, event.x, event.y),
        })
        #rect_id = self.map_canva.create_rectangle((self.lasx, self.lasy, event.x, event.y))
        self.lasx, self.lasy = event.x, event.y
 
    def save_zone_information(self):
        view_id = self.view_id + 1
        self.zone_data.save_map_information_to_table(
            view_id, self.title.get(), self.image_entry.get())


