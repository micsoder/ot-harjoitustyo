from tkinter import messagebox
from tkinter import *
import bcrypt

class Signup():

    def __init__(self, username_entry, password_entry, database):
        self.username_entry = username_entry
        self.password_entry = password_entry
        self.database = database

        self.create_account()

    def create_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username != '' and password != '':
            self.database.cursor.execute('SELECT username FROM users WHERE username = ?', [username])
            if self.database.cursor.fetchone() is not None:
                messagebox.showerror('Error', 'Username already exists.')
            else:
                encoded_password = password.encode('utf-8')
                hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
                self.database.cursor.execute('INSERT INTO users VALUES (?,?)', [username, hashed_password])
                self.database.connection.commit()
                messagebox.showinfo('Success', 'Account has been created.')
        else:
            messagebox.showerror('Error', 'Enter all information.')