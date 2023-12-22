import unittest
from unittest.mock import MagicMock
from logic.zone_data_handler import ZoneDataHandler
from tests.test_utility.test_database import TestDataBase
from ui.map_dashboard import MapDashboard
from ui.map_bar import MapBar
from ui.map_image import MapImage
from logic.map_page_handler import MapPageHandler
from database.insert_base_data import InsertBaseData


class TestZoneDataHandler(unittest.TestCase):

    def setUp(self):
        print('Testing starting...')
        self.test_database = TestDataBase()
        self.zone_data = ZoneDataHandler(self.test_database)
        self.zone_data.add_base_image_to_table(
            1, 'Marisong', 'Description', 'Marisong.png')

    def test_save_data_to_table_from_dashboard(self):

        self.zone_data.save_data_from_dashboard_to_table(
            1, 'Shire', 'A place where Hobbits live')

        fetched_zone_data = self.test_database.cursor.execute(
            "SELECT zone_title, zone_description FROM zone_base_data WHERE id = ?", (1,))

        zone_result = fetched_zone_data.fetchone()

        self.assertEqual(zone_result[0], 'Shire', 'A place where Hobbits live')

    def test_load_data_from_table_to_dashboard(self):

        result = self.zone_data.load_data_from_table_to_dashboard(1)
        zone_title, zone_description = result

        self.assertEqual(zone_title, 'Marisong')
        self.assertEqual(zone_description, 'Description')

    def test_add_base_image_to_table(self):

        self.zone_data.add_base_image_to_table(
            1, 'Marisong', 'Description', 'Marisong.png')

        fetched_zone_data = self.test_database.cursor.execute(
            "SELECT zone_title, zone_description, zone_image FROM zone_base_data WHERE id = ?", (1,))

        zone_result = fetched_zone_data.fetchone()

        expected_values = ('Marisong', 'Description', 'Marisong.png')
        self.assertEqual(zone_result, expected_values)

    def test_load_image_from_table_to_map(self):

        result = self.zone_data.load_image_from_table_to_map(1)
        self.assertEqual(result[0], 'Marisong.png')

    def test_save_new_zone_information_to_table(self):

        self.zone_data.save_new_zone_information_to_table(
            1, 'Ruins', 'The ruins are older than time', 'Ruins.png')

        fetched_new_zone_data = self.test_database.cursor.execute(
            "SELECT zone_title, zone_description, zone_image FROM zone_base_data WHERE id = ?", (2,))

        new_zone_result = fetched_new_zone_data.fetchone()
        expected_values = (
            'Ruins', 'The ruins are older than time', 'Ruins.png')
        self.assertEqual(new_zone_result, expected_values)

    def test_fetch_zone_titles_for_optionmenu(self):

        zone_titles = self.zone_data.fetch_zone_titles_for_optionmenu(1)
        self.assertEqual(zone_titles, [])

    def test_retrive_id_based_on_title(self):

        result = self.zone_data.retrive_id_based_on_title('Marisong')
        self.assertEqual(result, 1)
