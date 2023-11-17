import customtkinter
from tkinter import messagebox

class LoginFrame():

    def __init__(self, window, font1, font2, font3, font4, user_handler, switch_frame):
        self.window = window
        self.font1 = font1
        self.font2 = font2
        self.font3 = font3
        self.font4 = font4
        self.user_handler = user_handler
        self.switch_frame = switch_frame

        self.create_new_frame()
        self.create_username_entry()
        self.create_password_entry()
        self.create_login_label()
        self.create_login_button()

    def create_new_frame(self):
        print('Creating new frame')
        self.frame = customtkinter.CTkFrame(self.window, bg_color = '#001220', fg_color = '#001220', width = 570, height = 360)
        self.frame.place(x = 480, y = 200)

    def create_username_entry(self):
        self.username_entry = customtkinter.CTkEntry(self.frame, font = self.font2, text_color = '#fff', fg_color = '#001a2e', bg_color = '#121111', border_color = '#004780', border_width = 3, placeholder_text = 'Password', placeholder_text_color = '#a3a3a3', width = 200, height = 50)
        self.username_entry.place(x = 200, y = 80)
    
    def create_password_entry(self):
        self.password_entry = customtkinter.CTkEntry(self.frame, font = self.font2, show = '*', text_color = '#fff', fg_color = '#001a2e', bg_color = '#121111', border_color = '#004780', border_width = 3, placeholder_text = 'Username', placeholder_text_color = '#a3a3a3', width = 200, height = 50)
        self.password_entry.place(x = 200, y = 150)

    def create_login_label(self):
        login_label2 = customtkinter.CTkLabel(self.frame, font = self.font1, text = 'Log in', text_color = '#fff', bg_color = '#001220')
        login_label2.place(x = 200 , y = 20)
    
    def create_login_button(self):
        login_button2 = customtkinter.CTkButton(self.frame, command = self.login_button_pressed, font = self.font2, text_color = '#fff', text = 'Log in', fg_color = '#00965d', hover_color = '#006e44', bg_color = '#121111', cursor = 'hand2', corner_radius = 5, width = 120)
        login_button2.place(x = 200, y = 220)
    
    def login_button_pressed(self):
        success, message = self.user_handler.login(self.username_entry, self.password_entry)
        messagebox.showerror(success, message)

        self.frame.destroy()
        if callable(self.switch_frame):
            self.switch_frame(2)
        
