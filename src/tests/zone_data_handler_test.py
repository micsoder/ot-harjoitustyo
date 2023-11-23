import unittest
from unittest.mock import MagicMock
from logic.zone_data_handler import ZoneDataHandler
from tests.test_utility.test_database import TestDataBase
from ui.dashboard_base_frame import DashboardBaseFrame


class TestZoneDataHandler(unittest.TestCase):

    def setUp(self):
        print('Testing starting...')
        self.test_database = TestDataBase()
        self.zone_data = ZoneDataHandler(self.test_database)
    
    def test_save_data_to_table_from_dashboard(self):
        self.zone_data.save_data_from_dashboard_to_table('1', 'Shire', 'A place where Hobbits live')
        zone_data = self.test_database.cursor.execute(
            "SELECT zone_title, zone_description FROM zone_base_data WHERE id = 1")

        zone_result = zone_data.fetchone()
        self.assertEqual(zone_result[0], 'Shire', 'A place where Hobbits live')

    def test_load_data_from_table_to_dashboard(self):
        view_id = 1
        result = self.zone_data.load_data_from_table_to_dashboard(view_id)
        zone_title, zone_description = result

        self.assertEqual(zone_title, 'Shire')
        self.assertEqual(zone_description, 'A place where Hobbits live')