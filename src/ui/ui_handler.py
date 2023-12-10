from ui.signup_frame import SignupFrame
from ui.login_frame import LoginFrame
from ui.map_handler import MapHandler
from logic.user_handler import UserHandler
from logic.zone_data_handler import ZoneDataHandler
from logic.map_page_handler import MapPageHandler


class UiHandler():
    """Handles the user interface components and frame switching for the Atlas application.

    This class manages the creation and switching of different frames within the Atlas
    application's user interface. It interacts with the database and the lofic of user handler, zone data handler and map page handler.

    Attributes:
        window: The main application window.
        database: The database connection for the application.
        ui_utility: Utility functions for managing the user interface.
        user_handler: An instance of UserHandler for managing user-related logic.
        zone_data: An instance of ZoneDataHandler for handling zone-related logic.
        map_page: An instance of MapPageHandler for managing map page logic.

    Methods:
         __init__(self, window, database, ui_utility): Initializes the UiHandler with the
        provided window, database connection, and UI utility.
        switch_frame(self, frame_id): Switches the current frame based on the provided frame_id.
    """

    def __init__(self, window, database, ui_utility):
        """Initializes the UiHandler with the provided window, database connection, and UI utility."""
        self.window = window
        self.database = database
        self.ui_utility = ui_utility

        self.user_handler = UserHandler(self.database)
        self.zone_data = ZoneDataHandler(self.database)
        self.map_page = MapPageHandler(self.database)

        self.switch_frame(1)

    def switch_frame(self, frame_id):
        """Switches the current frame based on the provided frame_id which is the callback for the self.switch_frame parameter.

        Args:
            frame_id (int): The identifier for the frame to switch to.
        """
        if frame_id == 1:
            LoginFrame(self.window, self.user_handler,
                       self.switch_frame, self.ui_utility)
        if frame_id == 2:
            SignupFrame(self.window, self.user_handler,
                        self.switch_frame, self.ui_utility)
        if frame_id == 3:
            MapHandler(self.window, self.zone_data, self.map_page,
                       self.switch_frame, self.ui_utility)
