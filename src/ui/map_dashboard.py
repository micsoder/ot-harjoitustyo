import customtkinter
from ui.base_frame import BaseFrame
from database.create_tables import CreateTables
from logic.zone_data_handler import ZoneDataHandler


class MapDashboard(BaseFrame):

    def __init__(self, current_map_page_id, window, zone_data, ui_utility):
        super().__init__()
        self.current_map_page_id = current_map_page_id
        self.window = window
        self.zone_data = zone_data
        self.ui_utility = ui_utility

        self.width, self.height = self.ui_utility.get_size_in_relation_to_window(
            25, 100)
        self.x, self.y = self.ui_utility.get_size_in_relation_to_window(75, 0)

        self.background_dashboard_frame()
        self.title_entry()
        self.label()
        self.add_text_to_dashboard()
        self.save_text_button()
        self.load_data()

    def background_dashboard_frame(self):
        self.dashboard_frame = customtkinter.CTkFrame(
            self.window,
            bg_color=self.grey_blue,
            fg_color=self.grey_blue,
            width=self.width,
            height=self.height
        )

        self.dashboard_frame.place(x=self.x, y=self.y)

    def title_entry(self):
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

    def label(self):
        self.desc_label = customtkinter.CTkLabel(
            self.dashboard_frame,
            text="Description",
            font=self.font2,
            text_color=self.white,
            bg_color=self.grey_blue
        )
        self.desc_label.place(x=10, y=110)

    def add_text_to_dashboard(self):
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

    def save_text_button(self):
        self.save_button = customtkinter.CTkButton(
            self.dashboard_frame,
            text='Save',
            command=self.save_data,
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

    def load_data(self):
        zone_title, zone_description = self.zone_data.load_data_from_table_to_dashboard(
            self.current_map_page_id)
        self.title.insert(0, zone_title)
        self.description.insert("1.0", zone_description)

    def save_data(self):
        self.zone_data.save_data_from_dashboard_to_table(
            self.current_map_page_id, self.title.get(), self.description.get("1.0", "end-1c"))
