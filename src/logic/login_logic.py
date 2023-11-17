import customtkinter
from tkinter import messagebox
from tkinter import *
import bcrypt


class Login():

    def __init__(self, username_entry, password_entry, database):
        self.username_entry = username_entry
        self.password_entry = password_entry
        self.database = database
        self.login()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username != '' and password != '':
            self.database.cursor.execute('SELECT password FROM users WHERE username = ?', [username])
            result = self.database.cursor.fetchone()
            if result:
                if bcrypt.checkpw(password.encode('utf-8'), result[0]):
                    messagebox.showinfo('Success', 'Logged in successfully.')
                else: 
                    messagebox.showerror('Error', 'Invalid password.')
            else: 
                messagebox.showerror('Error', 'Invalid username.')
        else: 
            messagebox.showerror('Error', 'Enter all information.')