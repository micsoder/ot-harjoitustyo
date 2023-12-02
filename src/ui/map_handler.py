from ui.map_dashboard import MapDashboard
from ui.map_canva import MapCanva
from ui.map_bar import MapBar


class MapHandler():

    def __init__(self, window, zone_data, width, height, switch_state):
        self.window = window
        self.zone_data = zone_data
        self.width = width
        self.height = height
        self.switch_state = switch_state
        view_id = 1

        self.map_canva = MapCanva(view_id, self.window, self.zone_data, self.width, self.height)

        self.switch_frame(view_id)
    
    def switch_frame(self, view_id):
        self.map_canva.update_image(view_id)

        MapBar(view_id, self.window, self.zone_data, 
                    self.width, self.height, self.switch_frame)
        MapDashboard(view_id, self.window, self.zone_data, 
                    self.width, self.height)

       