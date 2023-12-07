import customtkinter
from tkinter import messagebox
from ui.base_frame import BaseFrame


class LoginFrame(BaseFrame):

    def __init__(self, window, user_handler, switch_frame):
        super().__init__()
        self.window = window
        self.user_handler = user_handler
        self.switch_frame = switch_frame

        self.create_new_frame()
        self.create_username_entry()
        self.create_password_entry()

        self.create_login_label()
        self.create_login_button()
        self.create_signup_label_to_next_page()
        self.create_signup_next_page_button()

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
            height=50
        )
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
            height=50
        )
        self.password_entry.place(x=200, y=150)

    def create_login_label(self):
        login_label2 = customtkinter.CTkLabel(
            self.frame,
            font=self.font1,
            text='Log in',
            text_color='#fff',
            bg_color='#001220')
        login_label2.place(x=200, y=20)

    def create_login_button(self):
        login_button2 = customtkinter.CTkButton(
            self.frame,
            command=self.login_button_pressed,
            font=self.font2, text_color='#fff',
            text='Log in',
            fg_color='#00965d',
            hover_color='#006e44',
            bg_color='#121111',
            cursor='hand2',
            corner_radius=5,
            width=120
        )
        login_button2.place(x=200, y=220)

    def create_signup_label_to_next_page(self):
        signup_label = customtkinter.CTkLabel(
            self.frame,
            font=self.font3,
            text="Don't have an account?",
            text_color='#fff',
            bg_color='#001220')
        signup_label.place(x=200, y=250)

    def create_signup_next_page_button(self):
        signup_button = customtkinter.CTkButton(
            self.frame,
            command=self.signup_button_pressed,
            font=self.font4,
            text_color='#00bf77',
            text='Sign up',
            fg_color='#001220',
            hover_color='#001220',
            cursor='hand2',
            width=40)
        signup_button.place(x=395, y=250)

    def login_button_pressed(self):
        success, message = self.user_handler.login(
            self.username_entry.get(), self.password_entry.get())
        if success == 'Success':
            messagebox.showinfo(success, message)
            self.frame.destroy()
            if callable(self.switch_frame):
                self.switch_frame(3)
        else:
            messagebox.showerror(success, message)


    def signup_button_pressed(self):
        self.frame.destroy()
        if callable(self.switch_frame):
            self.switch_frame(2)
