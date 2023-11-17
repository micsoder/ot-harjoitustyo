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
                return ('Error', 'Username already exists.')
            else:
                encoded_password = password.encode('utf-8')
                hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
                self.database.cursor.execute('INSERT INTO users VALUES (?,?)', [username, hashed_password])
                self.database.connection.commit()
                return ('Success', 'Account has been created.')
        else:
            return ('Error', 'Enter all information.')


    def login(self, username_entry, password_entry):
        username = username_entry.get()
        password = password_entry.get()
        if username != '' and password != '':
            self.database.cursor.execute('SELECT password FROM users WHERE username = ?', [username])
            result = self.database.cursor.fetchone()
            if result:
                if bcrypt.checkpw(password.encode('utf-8'), result[0]):
                    return ('Success', 'Logged in successfully.')
                else: 
                    return ('Error', 'Invalid password.')
            else: 
                return ('Error', 'Invalid username.')
        else: 
            return ('Error', 'Enter all information.')