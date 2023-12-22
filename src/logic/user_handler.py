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
        - admin_rights (int): 1 for true and 0 for false.

        Returns:
        Tuple[str, str]: A tuple containing the success and message.
        """

        if username == '' or password == '':
            return ("Error", "Enter all information.")

        if self.__user_exist_with_username(username):
            return ("Error", f"User with username {username} exists already")

        if self.__is_bad_password(password):
            return ("Error", "Password needs to be at least three characters long")

        hashed_password = self.__hash_password(password)

        if self.__new_account(username, hashed_password, admin_rights):
            return ('Success', 'Account has been created.')

        return ("Error", "An error occured when creating the account. Please try again.")

    def __hash_password(self, password):

        encoded_password = password.encode('utf-8')
        return bcrypt.hashpw(
            encoded_password, bcrypt.gensalt())

    def __new_account(self, username, hashed_password, admin_rights):
        try:
            self.database.cursor.execute('INSERT INTO users VALUES (?,?,?)', [
                username, hashed_password, admin_rights])
            self.database.connection.commit()
            return True
        except Exception as e:
            print(f"Error during database insertion: {e}")
            return False

    def __is_bad_password(self, password):
        # I know this is not a good criteria. It is just here for development reasons.
        if len(password) < 3:
            return True

        return False

    def login(self, username, password):
        """
        Authenticates a user with the provided username and password.

        Parameters:
        - username (str): The username for authentication.
        - password (str): The password for authentication. 

        Returns:
        Tuple[str, str]: A tuple containing the success and message.
        """

        if username == '' or password == '':
            return ('Error', 'Enter all information.')

        if self.__user_exist_with_username(username):
            if self.__validate_password(username, password):
                self.current_user = username
                return ("Success", "Logged in successfully.")

            return ('Error', 'Invalid password.')

        return ('Error', 'Invalid username.')

    def __user_exist_with_username(self, username):

        self.database.cursor.execute(
            'SELECT username FROM users WHERE username = ?', [username])
        result = self.database.cursor.fetchone()
        if result:
            return True
        return False

    def __validate_password(self, username, password):

        user_password = self.database.cursor.execute(
            'SELECT password FROM users WHERE username =?', [username]).fetchone()[0]

        if bcrypt.checkpw(password.encode('utf-8'), user_password):
            return True
        return False

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
