from tkinter import messagebox
import customtkinter
from ui.base_frame import BaseFrame

class SignupFrame(BaseFrame):

    def __init__(self, window, user_handler, switch_frame):
        super().__init__()
        self.window = window
        self.user_handler = user_handler
        self.switch_frame = switch_frame

        self.create_new_frame()
        self.create_username_entry()
        self.create_password_entry()

        self.create_signup_label()
        self.create_signup_button()
        self.create_login_label_to_next_page()
        self.create_login_next_page_button()

    def create_new_frame(self):
        self.frame = customtkinter.CTkFrame(
            self.window,
            bg_color='#001220',
            fg_color='#001220',
            width=570,
            height=360)
        self.frame.place(x=480, y=200)

    def create_username_entry(self):
        self.username_entry = customtkinter.CTkEntry(
            self.frame,
            font=self.font2,
            text_color='#fff',
            fg_color='#001a2e',
            bg_color='#121111',
            border_color='#004780',
            border_width=3,
            placeholder_text='Username',
            placeholder_text_color='#a3a3a3',
            width=200,
            height=50)
        self.username_entry.place(x=200, y=80)

    def create_password_entry(self):
        self.password_entry = customtkinter.CTkEntry(
            self.frame,
            font=self.font2,
            show='*',
            text_color='#fff',
            fg_color='#001a2e',
            bg_color='#121111',
            border_color='#004780',
            border_width=3,
            placeholder_text='Password',
            placeholder_text_color='#a3a3a3',
            width=200,
            height=50)
        self.password_entry.place(x=200, y=150)

    def create_signup_label(self):
        signup_label = customtkinter.CTkLabel(
            self.frame,
            font=self.font1,
            text='Create account',
            text_color='#fff',
            bg_color='#001220')
        signup_label.place(x=200, y=20)

    def create_signup_button(self):
        signup_button = customtkinter.CTkButton(
            self.frame,
            command=self.signup_button_pressed,
            font=self.font2,
            text_color='#fff',
            text='Create account',
            fg_color='#00965d',
            hover_color='#006e44',
            bg_color='#121111',
            cursor='hand2',
            corner_radius=5,
            width=120)
        signup_button.place(x=200, y=220)

    def create_login_label_to_next_page(self):
        login_label = customtkinter.CTkLabel(
            self.frame,
            font=self.font3,
            text='Already have an account?',
            text_color='#fff',
            bg_color='#001220')
        login_label.place(x=200, y=250)

    def create_login_next_page_button(self):
        login_button = customtkinter.CTkButton(
            self.frame,
            command=self.login_button_pressed,
            font=self.font4,
            text_color='#00bf77',
            text='Login',
            fg_color='#001220',
            hover_color='#001220',
            cursor='hand2',
            width=40)
        login_button.place(x=395, y=250)

    def signup_button_pressed(self):
        success, message = self.user_handler.create_account(
            self.username_entry.get(), self.password_entry.get())
        if success == 'Success':
            messagebox.showinfo(success, message)
        else:
            messagebox.showerror(success, message)

    def login_button_pressed(self):
        self.frame.destroy()
        if callable(self.switch_frame):
            self.switch_frame(1)

