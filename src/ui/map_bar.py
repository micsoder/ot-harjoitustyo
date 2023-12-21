import customtkinter
from ui.base_frame import BaseFrame


class MapBar(BaseFrame):

    def __init__(self, current_map_page_id, window, zone_data, map_page, switch_frame, ui_utility, map_image, map_dashboard):
        super().__init__()
        self.current_map_page_id = current_map_page_id
        self.window = window
        self.zone_data = zone_data
        self.map_page = map_page
        self.switch_frame = switch_frame
        self.ui_utility = ui_utility
        self.map_image = map_image
        self.map_dashboard = map_dashboard

        self.width, self.height = self.ui_utility.get_size_in_relation_to_window(75, 4)
        self.x, self.y = self.ui_utility.get_size_in_relation_to_window(0, 0)

        self.__create_map_bar_frame()
        self.__fetch_zone_titles_for_optionmenu()
        self.__show_zone_options()
        self.__add_zone_button()
        if self.current_map_page_id != 1:
            color = self.light_olive_green
        else:
            color = self.dark_olive_green
        self.__go_back_to_previous_map_button(color)
        self.__exit_map_view_button()

    def __create_map_bar_frame(self):
        self.map_bar_frame = customtkinter.CTkFrame(
            self.window,
            bg_color=self.grey_blue,
            fg_color=self.grey_blue,
            width=self.width,
            height=self.height
        )
        self.map_bar_frame.place(x=self.x, y=self.y)

    def __fetch_zone_titles_for_optionmenu(self):

        self.zone_titles_list = self.zone_data.fetch_zone_titles_for_optionmenu(
            self.current_map_page_id)

    def __show_zone_options(self):
        optionmenu_var = customtkinter.StringVar(value='Show zone')
        option_combobox = customtkinter.CTkOptionMenu(
            self.map_bar_frame,
            width=50,
            values=self.zone_titles_list,
            variable=optionmenu_var,
            command=self.__optionmenu_callback
        )

        option_combobox.place(x=self.width - 280, y=2)

    def __optionmenu_callback(self, selected_title):

        self.next_map_page_id = self.zone_data.retrive_id_based_on_title(
            selected_title)

        self.__switch_map_page_when_callback(self.next_map_page_id)

    def __switch_map_page_when_callback(self, map_page_id):

        if callable(self.switch_frame):
            print('Now displaying the selected map!')
            self.map_bar_frame.destroy()
            self.map_image.map_image_frame.destroy()
            self.map_dashboard.dashboard_frame.destroy()
            self.switch_frame(map_page_id)

    def __add_zone_button(self):
        self.add_zone_button = customtkinter.CTkButton(
            self.map_bar_frame,
            command=self.__zone_information_frame,
            text='Add zone',
            text_color=self.black,
            bg_color=self.grey_blue,
            fg_color=self.light_olive_green,
            border_color=self.light_olive_green,
            hover_color=self.dark_olive_green,
            cursor=self.hand2,
            corner_radius=5,
            width=30
        )

        self.add_zone_button.place(x=self.width - 70, y=2)

    def __zone_information_frame(self):
        self.information_frame = customtkinter.CTkFrame(
            self.window,
            bg_color=self.white,
            fg_color=self.white,
            width=250,
            height=250
        )
        self.information_frame.place(x=450, y=300)

        self.__zone_information_label()
        self.__zone_title_entry()
        self.__zone_image_file_entry()
        self.__zone_description_entry()
        self.__save_information_button()
        self.__cancel_zone_information_button()

    def __zone_information_label(self):
        self.zone_label = customtkinter.CTkLabel(
            self.information_frame,
            text="Zone Information",
            text_color=self.black,
            bg_color=self.white,
            fg_color=self.white,
        )
        self.zone_label.place(x=10, y=5)

    def __zone_title_entry(self):
        self.title = customtkinter.CTkEntry(
            self.information_frame,
            text_color=self.black,
            bg_color=self.white,
            fg_color=self.light_sage,
            border_color=self.light_sage,
            border_width=2,
            placeholder_text='Add title',
            placeholder_text_color=self.grey,
            width=220,
            height=20
        )
        self.title.place(x=10, y=40)

    def __zone_image_file_entry(self):
        self.image_entry = customtkinter.CTkEntry(
            self.information_frame,
            text_color=self.black,
            bg_color=self.white,
            fg_color=self.light_sage,
            border_color=self.light_sage,
            border_width=2,
            placeholder_text='Add image filename',
            placeholder_text_color=self.grey,
            width=220,
            height=20
        )
        self.image_entry.place(x=10, y=70)

    def __zone_description_entry(self):
        self.zone_description = customtkinter.CTkTextbox(
            self.information_frame,
            text_color=self.black,
            bg_color=self.white,
            fg_color=self.light_sage,
            border_color=self.light_sage,
            border_width=2,
            width=220,
            height=100,
            wrap='word'
        )
        self.zone_description.place(x=10, y=100)

    def __save_information_button(self):
        self.save_button = customtkinter.CTkButton(
            self.information_frame,
            text='Save',
            command=self.__save_zone_information,
            text_color=self.black,
            bg_color=self.white,
            fg_color=self.light_olive_green,
            border_color=self.light_olive_green,
            hover_color=self.dark_olive_green,
            cursor=self.hand2,
            corner_radius=5,
            width=30
        )
        self.save_button.place(x=10, y=210)

    def __save_zone_information(self):
        self.zone_data.save_new_zone_information_to_table(
            self.current_map_page_id, self.title.get(), self.zone_description.get("1.0", "end-1c"), self.image_entry.get())
        self.information_frame.destroy()
        self.__fetch_zone_titles_for_optionmenu()
        self.__show_zone_options()

    def __cancel_zone_information_button(self):
        self.cancel_button = customtkinter.CTkButton(
            self.information_frame,
            text='Cancel',
            command=self.__cancel_adding_of_zone_information,
            text_color=self.black,
            bg_color=self.white,
            fg_color=self.light_olive_green,
            border_color=self.light_olive_green,
            hover_color=self.dark_olive_green,
            cursor=self.hand2,
            corner_radius=5,
            width=30
        )
        self.cancel_button.place(x=60, y=210)

    def __cancel_adding_of_zone_information(self):
        self.information_frame.destroy()

    def __go_back_to_previous_map_button(self, color):
        self.go_back_button = customtkinter.CTkButton(
            self.map_bar_frame,
            command=self.__go_back_to_previous_map,
            text='Go back',
            text_color=self.black,
            bg_color=self.grey_blue,
            fg_color=color,
            border_color=self.light_olive_green,
            hover_color=self.dark_olive_green,
            cursor=self.hand2,
            corner_radius=5,
            width=30
        )
        self.go_back_button.place(x=self.width - 140, y=2)

    def __go_back_to_previous_map(self):

        if self.current_map_page_id != 1:

            self.previous_map_page_id = self.map_page.fetch_zone_parent_for_current_map(
                self.current_map_page_id)
            self.__switch_map_page_when_callback(self.previous_map_page_id)
        else:
            print('This is the parent map')

    def __exit_map_view_button(self):
        self.exit_button = customtkinter.CTkButton(
            self.map_bar_frame,
            command=self.__exit_view,
            text='Exit map view',
            text_color=self.black,
            bg_color=self.grey_blue,
            fg_color=self.light_olive_green,
            border_color=self.light_olive_green,
            hover_color=self.dark_olive_green,
            cursor=self.hand2,
            corner_radius=5,
            width=30
        )
        self.exit_button.place(x=2, y=2)

    def __exit_view(self):

        self.__switch_map_page_when_callback(False)
