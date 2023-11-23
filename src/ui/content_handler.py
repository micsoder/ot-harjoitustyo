from ui.dashboard_base_frame import DashboardBaseFrame
from ui.map_base_frame import MapBaseFrame


class ContentHandler():

    def __init__(self, window, zone_data, width, height, switch_state):
        self.window = window
        self.zone_data = zone_data
        self.width = width
        self.height = height
        self.switch_state = switch_state
        self.view_id = 1

        MapBaseFrame(self.view_id, self.window, self.zone_data, self.width, self.height)
        DashboardBaseFrame(self.view_id, self.window, self.zone_data, self.width, self.height)

    