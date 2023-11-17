from tkinter import messagebox
from tkinter import *
import bcrypt

class UserHandler():

    def __init__(self, database):
        self.database = database

    def create_account(self, username_entry, password_entry):
        username = username_entry.get()
        password = password_entry.get()

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


    def login(self, username_entry, password_entry):
        username = username_entry.get()
        password = password_entry.get()
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