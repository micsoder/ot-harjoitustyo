

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

    def add_base_image_to_table(self, view_id, title, description, image):
        self.database.cursor.execute(
            'SELECT * FROM zone_base_data WHERE id = ?', (view_id,))
        existing_data = self.database.cursor.fetchone()

        if existing_data:
            self.database.cursor.execute('''
                UPDATE zone_base_data
                SET zone_title = ?, zone_description = ?, zone_image = ? 
                WHERE id = ?''', (title, description, image, view_id))
        else:
            self.database.cursor.execute('''
                INSERT INTO zone_base_data (zone_title, zone_description, zone_image) 
                VALUES (?, ?, ?)''', (title, description, image, ))

        self.database.connection.commit()

    def load_image_from_table_to_map(self, view_id):
        self.database.cursor.execute(
            'SELECT zone_image FROM zone_base_data WHERE id = ?', (view_id,))
        data = self.database.cursor.fetchone()

        return data

    def save_new_zone_information_to_table(self, title, description, image):

        self.database.cursor.execute(
            'SELECT id FROM zone_base_data ORDER BY id DESC LIMIT 1')
        last_id = self.database.cursor.fetchone()[0]

        new_zone_id = last_id + 1

        self.database.cursor.execute(
            'SELECT * FROM zone_base_data WHERE id = ?', (new_zone_id,))
        existing_data = self.database.cursor.fetchone()

        if existing_data:
            self.database.cursor.execute('''
                UPDATE zone_base_data
                SET zone_title = ?, zone_description = ?, zone_image = ?
                WHERE id = ?''', (title, description, image, new_zone_id))
        else:
            self.database.cursor.execute('''
                INSERT INTO zone_base_data (id, zone_title, zone_description, zone_image) 
                VALUES (?, ?, ?, ?)''', (new_zone_id, title, description, image))

        self.database.connection.commit()

    def fetch_zone_titles_for_optionmenu(self):

        self.database.cursor.execute('SELECT zone_title FROM zone_base_data')
        zone_titles = [row[0] for row in self.database.cursor.fetchall()]
        return zone_titles

    def retrive_id_based_on_title(self, selected_title):
        self.database.cursor.execute(
            'SELECT id FROM zone_base_data WHERE zone_title = ?', (selected_title,))
        next_view_id = self.database.cursor.fetchone()[0]
        return next_view_id
