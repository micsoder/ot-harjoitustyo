class CreateTables():

    def __init__(self, database):
        self.database = database
        self.create_users_table()

    def create_users_table(self):

        self.database.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT NOT NULL,
                password TEXT NOT NULL)''')

    def create_information_table(self):

        self.database.cursor.execute('''
            CREATE TABLE IF NOT EXISTS information (
                - TEXT NOT NULL,
                - TEXT NOT NULL)''')
