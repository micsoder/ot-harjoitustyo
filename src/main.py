import customtkinter
from ui.ui_handler import UiHandler
from ui.ui_utility import UiUtility
from database.initialize_database import DataBase
from database.create_tables import CreateTables


class Main():
    """Main class for the Atlas application.

    This class initializes the main components of the Atlas application, including
    the root window, database connection, tables creation, UI utility, and UI view handler.

    Attributes:
        window (customtkinter.CTk): The main application window.
        screen_width (int): The width of the user's screen.
        screen_height (int): The height of the user's screen.
        database (DataBase): The database connection for the application.
        ui_utility (UiUtility): Utility functions for managing the user interface.

    Methods:
        __init__(): Initializes the main components of the Atlas application.
        create_root_window(): Creates and configures the main application window.
        create_database_connection(): Establishes a connection to the application database.
        create_all_tables(): Initializes the creation of all necessary database tables.
        create_ui_utility(): Creates an instance of UiUtility to manage UI-related functionalities.
        initialize_ui_view(): Initiates the UI view handler to manage the user interface.
    """

    def __init__(self):
        """Initialize the main components of the Atlas application."""
        self.__create_root_window()
        self.__create_database_connection()
        self.__create_all_tables()
        self.__create_ui_utility()
        self.__initialize_ui_view()
        self.window.mainloop()

    def __create_root_window(self):
        """Create and configure the main application window."""
        self.window = customtkinter.CTk()
        self.window.title('Atlas')

        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        self.window.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
        self.window.config(bg='#001220')

    def __create_database_connection(self):
        """Establish a connection to the application database."""
        self.database = DataBase()

    def __create_all_tables(self):
        """Initialize the creation of all necessary database tables."""
        CreateTables(self.database)

    def __create_ui_utility(self):
        """Create an instance of UiUtility to manage UI-related functionalities."""
        self.ui_utility = UiUtility(self.screen_width, self.screen_height)

    def __initialize_ui_view(self):
        """Initiate the UI view handler to manage the user interface."""
        UiHandler(self.window, self.database, self.ui_utility)
