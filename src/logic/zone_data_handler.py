

class ZoneDataHandler():

    def __init__(self, database):
        self.database = database

    def load_data_from_table(self, view_id, title_entry, description):

        self.database.cursor.execute('SELECT ZoneTitle, ZoneDescription FROM zone_base_data WHERE id = ?', (view_id,))
        data = self.database.cursor.fetchone()

        if data:
            ZoneTitle, ZoneDescription = data
            title_entry.insert(0, ZoneTitle)
            description.insert("1.0", ZoneDescription)

    def save_data_to_database(self, view_id, title, description):
        title = title.get()
        description = description.get("1.0", "end-1c")

        self.database.cursor.execute('SELECT * FROM zone_base_data WHERE id = ?', (view_id,))
        existing_data = self.database.cursor.fetchone()

        if existing_data:
            self.database.cursor.execute('''
                UPDATE zone_base_data
                SET ZoneTitle = ?, ZoneDescription = ? 
                WHERE id = ?''', (title, description, view_id))
        else:
            self.database.cursor.execute('''
                INSERT INTO zone_base_data (id, ZoneTitle, ZoneDescription) 
                VALUES (?, ?, ?)''', (view_id, title, description))

        self.database.connection.commit()