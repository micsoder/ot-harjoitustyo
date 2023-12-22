from ui.map_dashboard import MapDashboard
from ui.map_image import MapImage
from ui.map_bar import MapBar
from database.insert_base_data import InsertBaseData


class MapHandler():
    """Handler class for managing the map-related components in the Atlas application.

    This class initializes and coordinates the MapCanva, MapDashboard, and MapBar components
    for a specific map page in the Atlas application. It uses the provided zone_data, window,
    switch_state, and ui_utility to create and manage these components.

    Attributes:
        window: The main window of the Atlas application.
        zone_data: Data handler for zone-related information.
        map_page: Handler for managing map pages in the application.
        switch_state: Callback function for switching between application states.
        ui_utility: Utility class for handling UI-related functionality.

    Methods:
        __init__(self, window, zone_data, map_page, switch_state, ui_utility):
            Initializes the MapHandler with the provided parameters and sets up the initial map page.

        switch_frame(self, current_map_page_id):
            Switches the map frame based on the provided map page ID, creating the MapCanva,
            MapDashboard, and MapBar components for the specified map page.

    """

    def __init__(self, window, user_handler, zone_data, map_page, switch_state, ui_utility):
        """Initializes the MapHandler with the provided parameters and sets up the initial map page.

        Args:
            window: The main window of the Atlas application.
            zone_data: Data handler for zone-related information.
            map_page: Handler for managing map pages in the application.
            switch_state: Callback function for switching between application states.
            ui_utility: Utility class for handling UI-related functionality.
        """
        self.window = window
        self.user_handler = user_handler
        self.zone_data = zone_data
        self.map_page = map_page
        self.switch_state = switch_state
        self.ui_utility = ui_utility

        base_data = InsertBaseData(self.zone_data)
        base_data.add_base_image()

        current_map_page_id = 1

        self.switch_frame(current_map_page_id)

    def switch_frame(self, current_map_page_id):
        """Switches the map frame based on the provided map page ID.

        Creates and manages the MapCanva, MapDashboard, and MapBar components for the specified map page.

        Args:
            current_map_page_id: The ID of the current map page.
        """

        if current_map_page_id == False:
            if callable(self.switch_state):
                self.switch_state(1)

        else:
            map_image = MapImage(current_map_page_id,
                                 self.window, self.zone_data, self.ui_utility)
            map_dashboard = MapDashboard(
                current_map_page_id, self.window, self.user_handler, self.zone_data, self.ui_utility)

            MapBar(current_map_page_id, self.window, self.user_handler, self.zone_data, self.map_page,
                   self.switch_frame, self.ui_utility, map_image, map_dashboard)
