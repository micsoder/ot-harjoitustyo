from ui.signup_frame import SignupFrame
from ui.login_frame import LoginFrame
from ui.map_handler import MapHandler
from logic.user_handler import UserHandler
from logic.zone_data_handler import ZoneDataHandler
from logic.map_page_handler import MapPageHandler


class UiHandler():

    def __init__(self, window, database):

        self.window = window
        self.database = database

        # screen_width = self.window.winfo_screenwidth()
        # screen_height = self.window.winfo_screenheight()

        self.screen_width = 1536
        self.screen_height = 864

        self.user_handler = UserHandler(self.database)
        self.zone_data = ZoneDataHandler(self.database)
        self.map_page = MapPageHandler(self.database)

        self.switch_frame(1)

    def switch_frame(self, frame_id):
        if frame_id == 1:
            LoginFrame(self.window, self.user_handler, self.switch_frame)
        if frame_id == 2:
            SignupFrame(self.window, self.user_handler, self.switch_frame)
        if frame_id == 3:
            MapHandler(self.window, self.zone_data, self.map_page, self.screen_width,
                       self.screen_height, self.switch_frame)
