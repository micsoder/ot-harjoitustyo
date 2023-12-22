class CreateTables():
    """
    A class to manage the creation of tables in an SQLite database.

    Attributes:
    - database (DataBase): An instance of the DataBase class representing the SQLite database.
    """

    def __init__(self, database):
        """
        Initializes a new instance of the CreateTables class.

        Parameters:
        - database (DataBase): An instance of the DataBase class representing the SQLite database.
        """
        self.database = database
        self.__create_users_table()
        self.__create_zone_base_data_table()
        self.__create_map_page_table()

    def __create_users_table(self):
        """Private method to create the 'users' table in the SQLite database."""

        self.database.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                admin INTEGER)''')

    def __create_zone_base_data_table(self):
        """Private method to create the 'zone_base_data' table in the SQLite database."""

        self.database.cursor.execute('''
            CREATE TABLE IF NOT EXISTS zone_base_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                zone_title TEXT,
                zone_description TEXT,
                zone_image TEXT)''')

    def __create_map_page_table(self):
        """Private method to create the 'map_page' table in the SQLite database."""

        self.database.cursor.execute('''
            CREATE TABLE IF NOT EXISTS map_page (
                map_id INTEGER,
                zone_id INTEGER
                )''')
