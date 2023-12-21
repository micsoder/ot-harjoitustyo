class CreateTables():

    def __init__(self, database):
        self.database = database
        self.__create_users_table()
        self.__create_zone_base_data_table()
        self.__create_map_page_table()

    def __create_users_table(self):

        self.database.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT NOT NULL,
                password TEXT NOT NULL)''')

    def __create_zone_base_data_table(self):

        self.database.cursor.execute('''
            CREATE TABLE IF NOT EXISTS zone_base_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                zone_title TEXT,
                zone_description TEXT,
                zone_image TEXT)''')

    def __create_map_page_table(self):

        self.database.cursor.execute('''
            CREATE TABLE IF NOT EXISTS map_page (
                map_id INTEGER,
                zone_id INTEGER
                )''')
