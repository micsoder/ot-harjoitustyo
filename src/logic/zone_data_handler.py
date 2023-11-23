

class ZoneDataHandler():

    def __init__(self, database):
        self.database = database

    def load_data_from_table_to_dashboard(self, view_id):

        self.database.cursor.execute(
            'SELECT zone_title, zone_description FROM zone_base_data WHERE id = ?', (view_id,))
        data = self.database.cursor.fetchone()

        if data:
            zone_title, zone_description = data
            return zone_title, zone_description

    def save_data_from_dashboard_to_table(self, view_id, title, description):

        self.database.cursor.execute(
            'SELECT * FROM zone_base_data WHERE id = ?', (view_id,))
        existing_data = self.database.cursor.fetchone()

        if existing_data:
            self.database.cursor.execute('''
                UPDATE zone_base_data
                SET zone_title = ?, zone_description = ? 
                WHERE id = ?''', (title, description, view_id))
        else:
            self.database.cursor.execute('''
                INSERT INTO zone_base_data (id, zone_title, zone_description) 
                VALUES (?, ?, ?)''', (view_id, title, description))

        self.database.connection.commit()

    def add_image_data_to_table(self, view_id, image):
        self.database.cursor.execute(
            'SELECT * FROM zone_base_data WHERE id = ?', (view_id,))
        existing_data = self.database.cursor.fetchone()

        if existing_data:
            self.database.cursor.execute('''
                UPDATE zone_base_data
                SET zone_image = ? 
                WHERE id = ?''', (image, view_id))
        else:
            self.database.cursor.execute('''
                INSERT INTO zone_base_data (zone_image) 
                VALUES (?)''', (image, ))

    def load_data_from_table_to_map(self, view_id):
        self.database.cursor.execute(
            'SELECT zone_image FROM zone_base_data WHERE id = ?', (view_id,))
        data = self.database.cursor.fetchone()

        return data
