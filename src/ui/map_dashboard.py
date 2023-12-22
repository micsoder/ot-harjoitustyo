import customtkinter
from ui.base_frame import BaseFrame
from database.create_tables import CreateTables
from logic.zone_data_handler import ZoneDataHandler


class MapDashboard(BaseFrame):
    """
    The class that creates the dashboard for managing zone-related information.

    Attributes:
    - current_map_page_id (int): The identifier for the current map page.
    - window (tk.Tk): The main Tkinter window.
    - zone_data (ZoneDataHandler): An object providing data handling for zones.
    - ui_utility (UiUtility): An instance of the UiUtility class for UI-related utility functions.
    """

    def __init__(self, current_map_page_id, window, user_handler, zone_data, ui_utility):
        """
        Initializes a new instance of the MapDashboard class.

        Parameters:
        - current_map_page_id (int): The identifier for the current map page.
        - window (tk.Tk): The main Tkinter window.
        - zone_data (ZoneDataHandler): An object providing data handling for zones.
        - ui_utility (UiUtility): An instance of the UiUtility class for UI-related utility functions.
        """

        super().__init__()
        self.current_map_page_id = current_map_page_id
        self.window = window
        self.user_handler = user_handler
        self.zone_data = zone_data
        self.ui_utility = ui_utility

        self.width, self.height = self.ui_utility.get_size_in_relation_to_window(
            25, 100)
        self.x, self.y = self.ui_utility.get_size_in_relation_to_window(75, 0)

        self.__background_dashboard_frame()
        if self.user_handler.is_admin():
            self.__save_text_button()
            self.state = 'normal'
        else:
            self.state = 'disabled'
        self.__title_entry()
        self.__label() 
        self.__add_text_to_dashboard()
        self.__load_data()

    def __background_dashboard_frame(self):
        """Private method to create the frame for the dashboard."""

        self.dashboard_frame = customtkinter.CTkFrame(
            self.window,
            bg_color=self.grey_blue,
            fg_color=self.grey_blue,
            width=self.width,
            height=self.height
        )

        self.dashboard_frame.place(x=self.x, y=self.y)

    def __title_entry(self):
        """Private method to create the title entry widget in the dashboard."""

        self.title = customtkinter.CTkEntry(
            self.dashboard_frame,
            font=self.font1,
            text_color=self.white,
            fg_color=self.grey_blue,
            bg_color=self.grey_blue,
            border_color=self.white,
            border_width=2,
            placeholder_text='Title of mapview',
            placeholder_text_color=self.grey,
            width=350,
            height=70
        )
        self.title.place(x=10, y=20)

    def __label(self):
        """Private method to create the description label in the dashboard."""

        self.desc_label = customtkinter.CTkLabel(
            self.dashboard_frame,
            text="Description",
            font=self.font2,
            text_color=self.white,
            bg_color=self.grey_blue
        )
        self.desc_label.place(x=10, y=110)

    def __add_text_to_dashboard(self):
        """Private method to create the description text box in the dashboard."""

        self.description = customtkinter.CTkTextbox(
            self.dashboard_frame,
            font=self.font3,
            text_color=self.white,
            fg_color=self.grey_blue,
            bg_color=self.grey_blue,
            border_color=self.white,
            border_width=2,
            width=350,
            height=300,
            wrap='word')
        self.description.place(x=10, y=150)

    def __save_text_button(self):
        """Private method to create the save button in the dashboard."""

        self.save_button = customtkinter.CTkButton(
            self.dashboard_frame,
            text='Save',
            command=self.__save_data,
            font=self.font2,
            text_color=self.white,
            bg_color=self.grey_blue,
            fg_color=self.dentist_green,
            hover_color=self.dark_dentist_green,
            cursor=self.hand2,
            corner_radius=5,
            width=50
        )
        self.save_button.place(x=10, y=760)

    def __load_data(self):
        """ Private method to load data from the the zone_base_data table to the dashboard."""

        zone_title, zone_description = self.zone_data.load_data_from_table_to_dashboard(
            self.current_map_page_id)
        self.title.insert(0, zone_title)
        self.title.configure(state = self.state)
        self.description.insert("1.0", zone_description)
        self.description.configure(state = self.state)
    

    def __save_data(self):
        """Private method to save data from the dashboard to the zone."""

        self.zone_data.save_data_from_dashboard_to_table(
            self.current_map_page_id, self.title.get(), self.description.get("1.0", "end-1c"))
