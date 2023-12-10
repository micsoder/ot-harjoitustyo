import os


class UiUtility():

    def __init__(self, screen_width, screen_height):

        self.screen_width = screen_width
        self.screen_height = screen_height

    def get_size_in_relation_to_window(self, rel_width, rel_height):

        abs_width = rel_width * 0.01 * self.screen_width
        abs_height = rel_height * 0.01 * self.screen_height

        return abs_width, abs_height
