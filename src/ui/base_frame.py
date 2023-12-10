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
        self.font1 = ('Helvetica', 25, 'bold')
        self.font2 = ('Arial', 17, 'bold')
        self.font3 = ('Arial', 13, 'bold')
        self.font4 = ('Arial', 13, 'bold', 'underline')
