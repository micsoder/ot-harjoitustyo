from logic.map_page_handler import MapPageHandler


class ZoneDataHandler():
    """
    A class responsible for handling operations related to zone data in the database.

    Attributes:
    - database: An SQLite database connection and cursor.
    - map_page: An instance of the MapPageHandler class for managing map-page relationships.

    Methods:
    - __init__(self, database): Initializes the ZoneDataHandler with a database connection.
    - load_data_from_table_to_dashboard(self, view_id): Retrieves zone data for display on the dashboard.
    - save_data_from_dashboard_to_table(self, view_id, title, description): Saves zone data from the dashboard to the database.
    - add_base_image_to_table(self, view_id, title, description, image): Adds base image information to the database.
    - load_image_from_table_to_map(self, view_id): Retrieves the image file name for a given zone from the database.
    - save_new_zone_information_to_table(self, current_map_page_id, title, description, image): Saves new zone information to the database.
    - fetch_zone_titles_for_optionmenu(self, current_map_page_id): Retrieves zone titles for use in the OptionMenu.
    - retrive_id_based_on_title(self, selected_title): Retrieves the zone ID based on the selected title.
    """

    def __init__(self, database):
        """
        Initializes the ZoneDataHandler with a database connection.

        Parameters:
        - database: An SQLite database connection and cursor.
        """

        self.database = database
        self.map_page = MapPageHandler(self.database)

    def load_data_from_table_to_dashboard(self, view_id):
        """
        Retrieves zone data for display in the dashboard.

        Parameters:
        - view_id (int): The ID of the zone data to be retrieved.

        Returns:
        Tuple[str, str]: A tuple containing the zone title and description.
        """

        self.database.cursor.execute(
            'SELECT zone_title, zone_description FROM zone_base_data WHERE id = ?', (view_id,))
        data = self.database.cursor.fetchone()

        if data:
            zone_title, zone_description = data
            return zone_title, zone_description

    def save_data_from_dashboard_to_table(self, view_id, title, description):
        """
        Saves zone data from the dashboard to the database.

        Parameters:
        - view_id (int): The ID of the zone data to be updated or inserted.
        - title (str): The title of the zone.
        - description (str): The description of the zone.
        """

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
        """
        Adds base image information to the database.

        Parameters:
        - view_id (int): The ID of the zone data to be updated or inserted.
        - title (str): The title of the zone.
        - description (str): The description of the zone.
        - image (str): The filename of the image associated with the zone.
        """

        self.database.cursor.execute(
            'SELECT * FROM zone_base_data WHERE id = ?', (view_id,))
        existing_data = self.database.cursor.fetchone()
        if not existing_data:
            self.database.cursor.execute('''
                INSERT INTO zone_base_data (zone_title, zone_description, zone_image) 
                VALUES (?, ?, ?)''', (title, description, image, ))

        # else:
            # None

        self.database.connection.commit()

    def load_image_from_table_to_map(self, view_id):
        """
        Retrieves the image file name for a given zone from the database.

        Parameters:
        - view_id (int): The ID of the zone data.

        Returns:
        Tuple[str]: A tuple containing the image file name.
        """

        self.database.cursor.execute(
            'SELECT zone_image FROM zone_base_data WHERE id = ?', (view_id,))
        data = self.database.cursor.fetchone()

        return data

    def save_new_zone_information_to_table(self, current_map_page_id, title, description, image):
        """
        Saves new zone information to the database.

        Parameters:
        - current_map_page_id (int): The ID of the current map page.
        - title (str): The title of the new zone.
        - description (str): The description of the new zone.
        - image (str): The filename of the image associated with the new zone.
        """

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

        self.map_page.save_map_page_id(current_map_page_id, new_zone_id)

    def fetch_zone_titles_for_optionmenu(self, current_map_page_id):
        """
        Retrieves zone titles for use in the OptionMenu.

        Parameters:
        - current_map_page_id (int): The ID of the current map page.

        Returns:
        List[str]: A list containing the zone titles.
        """

        zone_ids = self.map_page.fetch_zone_ids_within_current_map_id(
            current_map_page_id)

        self.database.cursor.execute(
            'SELECT zone_title FROM zone_base_data WHERE id IN ({})'.format(
                ','.join(['?']*len(zone_ids))), zone_ids)
        zone_titles = [row[0] for row in self.database.cursor.fetchall()]

        return zone_titles

    def retrive_id_based_on_title(self, selected_title):
        """
        Retrieves the zone ID based on the selected title.

        Parameters:
        - selected_title (str): The selected zone title.

        Returns:
        int: The ID of the selected zone.
        """

        self.database.cursor.execute(
            'SELECT id FROM zone_base_data WHERE zone_title = ?', (selected_title,))
        next_view_id = self.database.cursor.fetchone()[0]
        return next_view_id
