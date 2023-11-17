from ui.create_signup_frame import CreateSignupFrame
from ui.create_login_frame import CreateLoginFrame


class UiHandler():

    def __init__(self, window, database):

        self.window = window
        self.database = database

        self.font1 = ('Helvetica', 25, 'bold')
        self.font2 = ('Arial', 17, 'bold')
        self.font3 = ('Arial', 13, 'bold')
        self.font4 = ('Arial', 13, 'bold', 'underline')

        self.create_signup_frame()

    def create_signup_frame(self):
        self.start = CreateSignupFrame(self.window, self.font1, self.font2, self.font3, self.font4, self.database, self.create_login_frame)

    def create_login_frame(self):
        CreateLoginFrame(self.window, self.font1, self.font2, self.font3, self.font4, self.database) 

    

        
    

