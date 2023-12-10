import customtkinter
from tkinter import messagebox
from ui.base_frame import BaseFrame


class LoginFrame(BaseFrame):

    def __init__(self, window, user_handler, switch_frame, ui_utility):
        super().__init__()
        self.window = window
        self.user_handler = user_handler
        self.switch_frame = switch_frame
        self.ui_utility = ui_utility

        self.new_frame()
        self.username_entry()
        self.password_entry()

        self.login_label()
        self.login_button()
        self.signup_label_to_next_page()
        self.signup_button_to_next_page()

    def new_frame(self):
        self.frame = customtkinter.CTkFrame(
            self.window,
            bg_color='#001220',
            fg_color='#001220',
            width=570,
            height=360
        )

        self.frame.pack_propagate(False)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

    def username_entry(self):
        self.username = customtkinter.CTkEntry(
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
        self.username.place(x=200, y=80)

    def password_entry(self):
        self.password = customtkinter.CTkEntry(
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
        self.password.place(x=200, y=150)

    def login_label(self):
        label = customtkinter.CTkLabel(
            self.frame,
            font=self.font1,
            text='Log in',
            text_color='#fff',
            bg_color='#001220')
        label.place(x=200, y=20)

    def login_button(self):
        button = customtkinter.CTkButton(
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
        button.place(x=200, y=220)

    def signup_label_to_next_page(self):
        signup_label = customtkinter.CTkLabel(
            self.frame,
            font=self.font3,
            text="Don't have an account?",
            text_color='#fff',
            bg_color='#001220')
        signup_label.place(x=200, y=250)

    def signup_button_to_next_page(self):
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
            self.username.get(), self.password.get())
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
