# -*- coding:utf-8 -*-

# CSS
# Define some color
c_BLACK = (0, 0, 0)
c_GRAY  = (55, 55, 55)
c_WHITE = (221, 221, 221)


class widget():
    """Template for every widget.
    """

    def __init__(self, game):
        """Initialization of the widget.
        """
        # Define needed properties
        self.name = ""
        self.x = 0
        self.y = 0

        # Save the pyGame reference
        self.game = game

    def update(self):
        pass

    # Define some tools
    def coo(self, x, y):
        return [self.x + x, self.y + y]
