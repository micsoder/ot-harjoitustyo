import customtkinter


class BaseFrame():
    """This class defines common attributes and fonts used in various frames
    within the Atlas application.

    Attributes:
        font1 (tuple): Font configuration for larger and bold text.
        font2 (tuple): Font configuration for medium-sized and bold text.
        font3 (tuple): Font configuration for smaller and bold text.
        font4 (tuple): Font configuration for underlined text.

    Methods:
        __init__(self): Initializes the BaseFrame with predefined fonts.
    """

    def __init__(self):
        """Initializes the BaseFrame with predefined fonts."""
        self.hand = 'hand2'

        self.font1 = ('Helvetica', 25, 'bold')
        self.font2 = ('Arial', 17, 'bold')
        self.font3 = ('Arial', 13, 'bold')
        self.font4 = ('Arial', 13, 'bold', 'underline')

        """Colors for login and signup frame"""
        self.black = '#000000'
        self.dark_blue = '#001220'
        self.midnight_blue = '#001a2e'
        self.ocean_blue = '#004780'
        self.grey = '#a3a3a3'
        self.dark_grey_black = '#121111'
        self.white = '#fff'

        self.light_dentist_green = '#00bf77'
        self.dentist_green = '#00965d'
        self.dark_dentist_green = '#006e44'

        """Dashboard colors"""

        self.grey_blue = '#3b5f7a'

        """Map bar colors"""

        self.light_olive_green = '#6EA149'
        self.dark_olive_green = '#56793C'
        self.light_sage = '#E5F0DD'