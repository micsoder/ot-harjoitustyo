from ui.map_dashboard import MapDashboard
from ui.map_canva import MapCanva
from ui.map_bar import MapBar


class MapHandler():

    def __init__(self, window, zone_data, map_page, width, height, switch_state):
        self.window = window
        self.zone_data = zone_data
        self.map_page = map_page
        self.width = width
        self.height = height
        self.switch_state = switch_state
        current_map_page_id = 1

        self.map_canva = MapCanva(
            current_map_page_id, self.window, self.zone_data, self.width, self.height)

        self.switch_frame(current_map_page_id)

    def switch_frame(self, current_map_page_id):
        self.map_canva.update_image(current_map_page_id)

        MapBar(current_map_page_id, self.window, self.zone_data,
               self.width, self.height, self.switch_frame)
        MapDashboard(current_map_page_id, self.window, self.zone_data,
                     self.width, self.height)
