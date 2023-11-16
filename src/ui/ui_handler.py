from ui.create_account_frame import CreateAccountFrame
from ui.create_login_frame import CreateLoginFrame

class UiHandler():

    def __init__(self, window):

        self.window = window

        self.font1 = ('Helvetica', 25, 'bold')
        self.font2 = ('Arial', 17, 'bold')
        self.font3 = ('Arial', 13, 'bold')
        self.font4 = ('Arial', 13, 'bold', 'underline')

        self.create_account_frame()

    def create_account_frame(self):
        self.start= CreateAccountFrame(self.window, self.font1, self.font2, self.font3, self.font4, self.login_button_pressed)

    def login_button_pressed(self):
        self.show_create_login_frame()

    def show_create_login_frame(self):
        CreateLoginFrame(self.window, self.font1, self.font2, self.font3, self.font4) 
    

        
    

