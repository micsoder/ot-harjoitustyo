import os


class UiUtility():
    """
    A utility class for managing UI-related tasks, such as calculating absolute dimensions
    in relation to the screen size.

    Attributes:
    - screen_width (int): The width of the screen or window in pixels.
    - screen_height (int): The height of the screen or window in pixels.
    """

    def __init__(self, screen_width, screen_height):
        """
        Initializes a new instance of the UiUtility class.

        Parameters:
        - screen_width (int): The width of the screen or window in pixels.
        - screen_height (int): The height of the screen or window in pixels.
        """

        self.screen_width = screen_width
        self.screen_height = screen_height

    def get_size_in_relation_to_window(self, rel_width, rel_height):
        """
        Calculates the absolute dimensions in pixels based on relative dimensions and
        the screen size.

        Parameters:
        - rel_width (float): The relative width as a percentage of the screen width.
        - rel_height (float): The relative height as a percentage of the screen height.

        Returns:
        Tuple[float]: A tuple containing the screen abs width and height.

        """

        abs_width = rel_width * 0.01 * self.screen_width
        abs_height = rel_height * 0.01 * self.screen_height

        return abs_width, abs_height
