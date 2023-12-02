import customtkinter


class MapBar():

    def __init__(self, view_id, window, zone_data, width, height, switch_frame):
        self.view_id = view_id
        self.window = window
        self.zone_data = zone_data
        self.width = width
        self.height = height
        self.switch_frame = switch_frame

        self.create_map_bar_frame()
        self.fetch_zone_titles_for_optionmenu()
        self.show_zone_options()
        self.add_zone_button()

    def create_map_bar_frame(self):
        self.map_bar_frame = customtkinter.CTkFrame(
            self.window,
            bg_color='#3b5f7a',
            fg_color='#3b5f7a',
            width=self.width * 3/4,
            height=self.height * 1/27
        )
        self.map_bar_frame.pack(anchor='nw')

    def fetch_zone_titles_for_optionmenu(self):

        self.zone_titles_list = self.zone_data.fetch_zone_titles_for_optionmenu()

    def show_zone_options(self):
        optionmenu_var = customtkinter.StringVar(value='Show zone')
        option_combobox = customtkinter.CTkOptionMenu(
            self.map_bar_frame,
            width=50,
            values=self.zone_titles_list,
            variable=optionmenu_var,
            command=self.optionmenu_callback
        )

        option_combobox.place(x=950, y=2)

    def optionmenu_callback(self, selected_title):

        self.next_view_id = self.zone_data.retrive_id_based_on_title(
            selected_title)

        if callable(self.switch_frame):
            print('Now displaying the selected map!')
            self.map_bar_frame.destroy()
            self.switch_frame(self.next_view_id)

    def add_zone_button(self):
        self.add_zone_button = customtkinter.CTkButton(
            self.map_bar_frame,
            command=self.zone_information_frame,
            text='Add zone',
            text_color='black',
            bg_color='#3b5f7a',
            fg_color='#6EA149',
            border_color='#6EA149',
            hover_color='#56793C',
            cursor='hand2',
            corner_radius=5,
            width=30
        )
        self.add_zone_button.place(x=1085, y=2)

    def zone_information_frame(self):
        self.information_frame = customtkinter.CTkFrame(
            self.window,
            bg_color='#FFFFFF',
            fg_color='#FFFFFF',
            width=250,
            height=250
        )
        self.information_frame.place(x=450, y=300)

        self.zone_information_label()
        self.zone_title_entry()
        self.zone_image_file_entry()
        self.zone_description_entry()
        self.save_information_button()

    def zone_information_label(self):
        self.zone_label = customtkinter.CTkLabel(
            self.information_frame,
            text="Zone Information",
            text_color='black',
            bg_color='#FFFFFF',
            fg_color='#FFFFFF',
        )
        self.zone_label.place(x=10, y=5)

    def zone_title_entry(self):
        self.title = customtkinter.CTkEntry(
            self.information_frame,
            text_color='black',
            bg_color='#FFFFFF',
            fg_color='#E5F0DD',
            border_color='#E5F0DD',
            border_width=2,
            placeholder_text='Add title',
            placeholder_text_color='#a3a3a3',
            width=220,
            height=20
        )
        self.title.place(x=10, y=40)

    def zone_image_file_entry(self):
        self.image_entry = customtkinter.CTkEntry(
            self.information_frame,
            text_color='black',
            bg_color='#FFFFFF',
            fg_color='#E5F0DD',
            border_color='#E5F0DD',
            border_width=2,
            placeholder_text='Add image filename',
            placeholder_text_color='#a3a3a3',
            width=220,
            height=20
        )
        self.image_entry.place(x=10, y=70)

    def zone_description_entry(self):
        self.zone_description = customtkinter.CTkTextbox(
            self.information_frame,
            text_color='black',
            bg_color='#FFFFFF',
            fg_color='#E5F0DD',
            border_color='#E5F0DD',
            border_width=2,
            width=220,
            height=100,
            wrap='word'
        )
        self.zone_description.place(x=10, y=100)

    def save_information_button(self):
        self.save_button = customtkinter.CTkButton(
            self.information_frame,
            text='Save',
            command=self.save_zone_information,
            text_color='black',
            bg_color='#FFFFFF',
            fg_color='#6EA149',
            border_color='#6EA149',
            hover_color='#56793C',
            cursor='hand2',
            corner_radius=5,
            width=30
        )
        self.save_button.place(x=10, y=210)

    def save_zone_information(self):
        self.zone_data.save_new_zone_information_to_table(
            self.view_id, self.title.get(), self.zone_description.get("1.0", "end-1c"), self.image_entry.get())
        self.information_frame.destroy()
        self.fetch_zone_titles_for_optionmenu()
        self.show_zone_options()
