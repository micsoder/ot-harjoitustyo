from ui.signup_frame import SignupFrame
from ui.login_frame import LoginFrame
from ui.content_handler import ContentHandler
from logic.user_handler import UserHandler
from logic.zone_data_handler import ZoneDataHandler


class UiHandler():

    def __init__(self, window, database):

        self.window = window
        self.database = database

        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        self.user_handler = UserHandler(self.database)
        self.zone_data = ZoneDataHandler(self.database)

        self.switch_frame(0)

    def switch_frame(self, frame_id):
        if frame_id == 0:
            SignupFrame(self.window, self.user_handler, self.switch_frame)
        if frame_id == 1:
            LoginFrame(self.window, self.user_handler, self.switch_frame)
        if frame_id == 2:
            ContentHandler(self.window, self.zone_data, self.screen_width,
                           self.screen_height, self.switch_frame)
