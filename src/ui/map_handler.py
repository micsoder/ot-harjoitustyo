from ui.map_dashboard import MapDashboard
from ui.map_canva import MapCanva
from ui.map_bar import MapBar
from database.insert_data import InsertData


class MapHandler():

    def __init__(self, window, zone_data, map_page, switch_state, ui_utility):
        self.window = window
        self.zone_data = zone_data
        self.map_page = map_page
        self.switch_state = switch_state
        self.ui_utility = ui_utility

        base_data = InsertData(self.zone_data)
        base_data.add_base_image()

        current_map_page_id = 1
        
        self.switch_frame(current_map_page_id)

    def switch_frame(self, current_map_page_id):
        if current_map_page_id == False:
            if callable(self.switch_state):
                self.switch_state(1)
        
        else:
            map_canva = MapCanva(current_map_page_id, self.window, self.zone_data, self.ui_utility)
            map_dashboard = MapDashboard(current_map_page_id, self.window, self.zone_data, self.ui_utility)

            MapBar(current_map_page_id, self.window, self.zone_data, self.map_page, self.switch_frame, self.ui_utility, map_canva, map_dashboard)
