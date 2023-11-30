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

        self.switch_frame()
    
    def switch_frame(self):

        MapBaseFrame(self.view_id, self.window,
                     self.zone_data, self.width, self.height)
        DashboardBaseFrame(self.view_id, self.window,
                           self.zone_data, self.width, self.height)

        """ The methods below will be used to determine and change the self.view_id but this functionality will be made next week. """

    def leftClick():
        """ Zoom in."""
        pass

    def rightClick():
        """ Zoom out. """
        pass

    def middleClick():
        """ Add object. """
        pass

    def ctrlRightClick(self):
        """ Add object. """
        pass
