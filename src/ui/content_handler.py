from ui.dashboard_base_frame import DashboardBaseFrame
from ui.map_base_frame import MapBaseFrame
from ui.map_bar_frame import MapBarFrame


class ContentHandler():

    def __init__(self, window, zone_data, width, height, switch_state):
        self.window = window
        self.zone_data = zone_data
        self.width = width
        self.height = height
        self.switch_state = switch_state
        view_id = 1

        self.map_base_frame = MapBaseFrame(view_id, self.window, self.zone_data, self.width, self.height)

        self.switch_frame(view_id)
    
    def switch_frame(self, view_id):
        self.map_base_frame.update_image(view_id)

        MapBarFrame(view_id, self.window, self.zone_data, 
                    self.width, self.height, self.switch_frame)
        DashboardBaseFrame(view_id, self.window, self.zone_data, 
                    self.width, self.height)

       