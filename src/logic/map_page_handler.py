
class MapPageHandler():
    """
    A class responsible for handling map page-related operations in the database.

    Attributes:
    - database: An SQLite database connection and cursor.

    Methods:
    - __init__(self, database): Initializes the MapPageHandler with a database connection.
    - save_map_page_id(self, current_map_page_id, new_zone_id): Saves a mapping between a map page and a zone in the database.
    - fetch_zone_ids_within_current_map_id(self, current_map_page_id): Retrieves the zone IDs within a specified map page.
    - fetch_zone_parent_for_current_map(self, current_map_page_id): Retrieves the parent map page ID for a specified zone within a map.
    """

    def __init__(self, database):
        """
        Initializes the MapPageHandler with a database connection.

        Parameters:
        - database: An SQLite database connection and cursor.
        """

        self.database = database

    def save_map_page_id(self, current_map_page_id, new_zone_id):
        """
        Saves a mapping between a map page and a zone in the database.

        Parameters:
        - current_map_page_id (int): The ID of the current map page.
        - new_zone_id (int): The ID of the new zone to be associated with the map page.
        """

        self.database.cursor.execute('''
                INSERT INTO map_page (map_id, zone_id) 
                VALUES (?, ?)''', (current_map_page_id, new_zone_id))

        self.database.connection.commit()

    def fetch_zone_ids_within_current_map_id(self, current_map_page_id):
        """
        Retrieves the zone IDs within a specified map page.

        Parameters:
        - current_map_page_id (int): The ID of the current map page.

        Returns:
        List[int]: A list of zone IDs.
        """

        self.database.cursor.execute(
            'SELECT zone_id FROM map_page WHERE map_id = ?', (current_map_page_id,))
        zone_ids = [row[0] for row in self.database.cursor.fetchall()]
        return zone_ids

    def fetch_zone_parent_for_current_map(self, current_map_page_id):
        """
        Retrieves the parent map page ID for a specified zone within a map.

        Parameters:
        - current_map_page_id (int): The ID of the current map page.

        Returns:
        int: Interger of previous map page ID.
        """

        self.database.cursor.execute(
            'SELECT map_id FROM map_page WHERE zone_id = ?', (current_map_page_id,))
        previous_map_page_id = self.database.cursor.fetchone()[0]

        return previous_map_page_id
