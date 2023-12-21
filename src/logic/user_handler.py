import bcrypt


class UserHandler():
    """
    A class responsible for handling user account creation and login operations.

    Attributes:
    - database: An SQLite database connection and cursor.

    Methods:
    - __init__(self, database): Initializes the UserHandler with a database connection.
    - create_account(self, username, password): Creates a new user account with the given username and password.
    - login(self, username, password): Authenticates a user with the provided username and password.
    """

    def __init__(self, database):
        """
        Initializes the UserHandler with a database connection.

        Parameters:
        - database: An SQLite database connection and cursor.
        """
        self.database = database

    def create_account(self, username, password):
        """
        Creates a new user account with the given username and password.

        Parameters:
        - username (str): The username for the new account.
        - password (str): The password for the new account.

        Returns:
        Tuple[str, str]: A tuple containing the success and message.
        """

        if username != '' and password != '':
            self.database.cursor.execute(
                'SELECT username FROM users WHERE username = ?', [username])
            if self.database.cursor.fetchone() is not None:
                return ('Error', 'Username already exists.')
            else:
                encoded_password = password.encode('utf-8')
                hashed_password = bcrypt.hashpw(
                    encoded_password, bcrypt.gensalt())
                self.database.cursor.execute('INSERT INTO users VALUES (?,?)', [
                                             username, hashed_password])
                self.database.connection.commit()
                return ('Success', 'Account has been created.')
        else:
            return ('Error', 'Enter all information.')

    def login(self, username, password):
        """
        Authenticates a user with the provided username and password.

        Parameters:
        - username (str): The username for authentication.
        - password (str): The password for authentication. 
                
        Returns:
        Tuple[str, str]: A tuple containing the success and message.
        """

        if username != '' and password != '':
            self.database.cursor.execute(
                'SELECT password FROM users WHERE username = ?', [username])
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
