from tkinter import messagebox
import tkinter as tk
import customtkinter
from ui.base_frame import BaseFrame


class SignupFrame(BaseFrame):
    """Frame for user signup in the Atlas application.

    This class handles the UI components related to user signup, including entry fields
    for username and password, signup button, and navigation to the login page.

    Attributes:
        window: The main application window.
        user_handler: An instance of UserHandler for managing user-related logic.
        switch_frame: A function for switching between different frames.
        ui_utility: Utility functions for managing the user interface.

    Methods:
        __init__(self, window, user_handler, switch_frame, ui_utility):
            Initializes the SignupFrame with the provided parameters.
        new_frame(self): Creates a new frame for the signup interface.
        username_entry(self): Creates an entry field for the username.
        password_entry(self): Creates an entry field for the password.
        signup_label(self): Creates a label for the signup section.
        signup_button(self): Creates a button for initiating the signup process.
        login_label_to_next_page(self): Creates a label prompting users to log in.
        login_button_to_next_page(self): Creates a button for navigating to the login page.
        signup_button_pressed(self): Handles the signup button press event.
        login_button_pressed(self): Handles the login button press event.
    """

    def __init__(self, window, user_handler, switch_frame, ui_utility):
        """Initializes the SignupFrame with the provided parameters."""
        super().__init__()
        self.window = window
        self.user_handler = user_handler
        self.switch_frame = switch_frame
        self.ui_utility = ui_utility

        self.admin_rights = 0

        self.__new_frame()
        self.__username_entry()
        self.__password_entry()

        self.__signup_label()
        self.__signup_button()
        self.__admin_checkbox()
        self.__login_label_to_next_page()
        self.__login_button_to_next_page()

    def __new_frame(self):
        """Creates a new frame for the signup interface."""
        self.frame = customtkinter.CTkFrame(
            self.window,
            bg_color=self.dark_blue,
            fg_color=self.dark_blue,
            width=570,
            height=360
        )

        self.frame.pack_propagate(False)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

    def __username_entry(self):
        """Creates an entry field for the username."""
        self.username = customtkinter.CTkEntry(
            self.frame,
            font=self.font2,
            text_color=self.white,
            fg_color=self.midnight_blue,
            bg_color=self.dark_grey_black,
            border_color=self.ocean_blue,
            border_width=3,
            placeholder_text='Username',
            placeholder_text_color=self.grey,
            width=200,
            height=50)
        self.username.place(x=200, y=80)

    def __password_entry(self):
        """Creates an entry field for the password."""
        self.password = customtkinter.CTkEntry(
            self.frame,
            font=self.font2,
            show='*',
            text_color=self.white,
            fg_color=self.midnight_blue,
            bg_color=self.dark_grey_black,
            border_color=self.ocean_blue,
            border_width=3,
            placeholder_text='Password',
            placeholder_text_color=self.grey,
            width=200,
            height=50)
        self.password.place(x=200, y=150)

    def __signup_label(self):
        """Creates a label for the signup section."""
        label = customtkinter.CTkLabel(
            self.frame,
            font=self.font1,
            text='Create account',
            text_color=self.white,
            bg_color=self.dark_blue)
        label.place(x=200, y=20)

    def __signup_button(self):
        """Creates a button for initiating the signup process."""
        button = customtkinter.CTkButton(
            self.frame,
            command=self.__signup_button_pressed,
            font=self.font2,
            text_color=self.white,
            text='Create account',
            fg_color=self.dentist_green,
            hover_color=self.dark_dentist_green,
            bg_color=self.dark_grey_black,
            cursor=self.hand2,
            corner_radius=5,
            width=120)
        button.place(x=200, y=220)
    
    def __admin_checkbox(self):
        self.chk_var = customtkinter.IntVar()
        self.admin_checkbox = customtkinter.CTkCheckBox(
            self.frame, 
            text='Admin',
            font=self.font3, 
            variable = self.chk_var, 
            command=self.__admin_checkbox_clicked,
            text_color=self.white,
            fg_color=self.midnight_blue,
            border_color=self.ocean_blue,
            border_width=3)

        self.admin_checkbox.place(x=370, y=220)
    
    def __admin_checkbox_clicked(self):
        self.admin_rights = self.chk_var.get()
        print('Creating admin account with admin_rights:', self.admin_rights)
        

    def __login_label_to_next_page(self):
        """Creates a label prompting users to log in."""
        login_label = customtkinter.CTkLabel(
            self.frame,
            font=self.font3,
            text='Already have an account?',
            text_color=self.white,
            bg_color=self.dark_blue)
        login_label.place(x=200, y=250)

    def __login_button_to_next_page(self):
        """Creates a button for navigating to the login page."""
        login_button = customtkinter.CTkButton(
            self.frame,
            command=self.__login_button_pressed,
            font=self.font4,
            text_color=self.light_dentist_green,
            text='Login',
            fg_color=self.dark_blue,
            hover_color=self.dark_blue,
            cursor=self.hand2,
            width=40)
        login_button.place(x=395, y=250)

    def __signup_button_pressed(self):
        """Handles the signup by calling the user_handler logic."""
        success, message = self.user_handler.create_account(
            self.username.get(), self.password.get(), self.admin_rights)
        if success == 'Success':
            messagebox.showinfo(success, message)
        else:
            messagebox.showerror(success, message)

    def __login_button_pressed(self):
        """Handles the event when user returns to login page by destroying the current frame and calling the switch_frame method with the frame_id of the login page."""
        self.frame.destroy()
        if callable(self.switch_frame):
            self.switch_frame(1)
