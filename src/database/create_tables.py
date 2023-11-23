class CreateTables():

    def __init__(self, database):
        self.database = database
        self.create_users_table()
        self.create_zone_base_data_table()

    def create_users_table(self):

        self.database.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT NOT NULL,
                password TEXT NOT NULL)''')

    def create_zone_base_data_table(self):

        self.database.cursor.execute('''
            CREATE TABLE IF NOT EXISTS zone_base_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                zone_title TEXT,
                zone_description TEXT,
                zone_image TEXT)''')
