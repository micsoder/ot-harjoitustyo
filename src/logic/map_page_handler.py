
class MapPageHandler():

    def __init__(self, database):

        self.database = database

    def save_map_page_id(self, current_map_page_id, new_zone_id):

        self.database.cursor.execute('''
                INSERT INTO map_page (map_id, zone_id) 
                VALUES (?, ?)''', (current_map_page_id, new_zone_id))

        self.database.connection.commit()

    def fetch_zone_ids_within_current_map_id(self, current_map_page_id):

        self.database.cursor.execute(
            'SELECT zone_id FROM map_page WHERE map_id = ?', (current_map_page_id,))
        zone_ids = [row[0] for row in self.database.cursor.fetchall()]

        return zone_ids

    def fetch_zone_parent_for_current_map(self, current_map_page_id):

        self.database.cursor.execute(
            'SELECT map_id FROM map_page WHERE zone_id = ?', (current_map_page_id,))
        previous_map_page_id = self.database.cursor.fetchone()[0]

        return previous_map_page_id
