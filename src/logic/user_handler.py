import bcrypt


class UserHandler():
    """
    A class responsible for handling user account creation and login operations.

    Attributes:
    - database: An SQLite database connection and cursor.

    Methods:
    - __init__(self, database): Initializes the UserHandler with a database connection.
    - create_account(self, username, password): Creates account with username and password.
    - login(self, username, password): Authenticates a user with the provided username and password.
    - is_admin(self): Returns true or false if user is admin or not.
    """

    def __init__(self, database):
        """
        Initializes the UserHandler with a database connection.

        Parameters:
        - database: An SQLite database connection and cursor.
        """
        self.database = database
        self.current_user = None

    def create_account(self, username, password, admin_rights):
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

            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(
                encoded_password, bcrypt.gensalt())
            self.database.cursor.execute('INSERT INTO users VALUES (?,?,?)', [
                username, hashed_password, admin_rights])
            self.database.connection.commit()
            return ('Success', 'Account has been created.')

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
                    self.current_user = username
                    return ('Success', 'Logged in successfully.')

                return ('Error', 'Invalid password.')

            return ('Error', 'Invalid username.')

        return ('Error', 'Enter all information.')

    def is_admin(self):
        """
        Checks whether current user is admin or not.

        Returns:
        Boolen
        """

        self.database.cursor.execute(
            'SELECT admin FROM users WHERE username = ?', [self.current_user])
        admin = self.database.cursor.fetchone()

        if admin[0] == 1:
            return True

        return False
