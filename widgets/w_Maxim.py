# -*- coding:utf-8 -*-

from widgets.widget import *

class w_Maxim(widget):
    """Widget - Maxim
    Display a maxim at the bottom of the screen
    """

    def __init__(self, game):
        """Initialize the widget.
        """
        widget.__init__(self, game)

        # Update needed properties
        self.name = "w_Maxim"
        self.x = 0
        self.y = 0

        # Define some font
        self.font = self.game.font.SysFont(
                'Helvetica', 25, bold=False, italic=False)

    def update(self, screen):
        str_maxim = u"La réponse est 42."
        str_maxim_size = self.font.size(str_maxim)

        txt_maxim = self.font.render(str_maxim, True, c_WHITE)

        line_x_s = screen.get_size()[0]*0.3
        line_x_e = screen.get_size()[0]*0.7
        line_y = screen.get_size()[1]-120
        self.game.draw.line(screen, c_WHITE,
                [line_x_s, line_y], [line_x_e, line_y], 1)

        txt_x = screen.get_size()[0]/2 - self.font.size(str_maxim)[0]/2
        txt_y = screen.get_size()[1] - 100
        screen.blit(txt_maxim, self.coo(txt_x, txt_y))
