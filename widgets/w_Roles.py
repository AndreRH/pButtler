# -*- coding:utf-8 -*-

from widgets.widget import *

class w_Roles(widget):
    """Widget - Roles
    Display the roles planning.
    """

    def __init__(self, game, screen):
        """Initialize the widget.
        """
        widget.__init__(self, game, screen)

        # Update needed properties
        self.name = "w_Roles"
        self.x = 150
        self.y = 180

        # Define some font
        self.font = self.game.font.SysFont(
                'Helvetica', 18, bold=False, italic=False)

    def update(self, screen, t):
        txt_repas = self.font.render("Repas", True, c_GRAY)
        txt_MH = self.font.render("MH", True, c_GRAY)
        txt_MB = self.font.render("MB", True, c_GRAY)

        txt_repas_val = self.font.render(
                "Domitille / Jean-Baptise", True, c_WHITE)
        txt_MH_val = self.font.render("Reda", True, c_WHITE)
        txt_BH_val = self.font.render("Antoine", True, c_WHITE)

        screen.blit(txt_repas,
                self.coo(80 - self.font.size("Repas")[0], 0))
        screen.blit(txt_MH,
                self.coo(80 - self.font.size("MH")[0], 30))
        screen.blit(txt_MB,
                self.coo(80 - self.font.size("MB")[0], 60))

        screen.blit(txt_repas_val, self.coo(90, 0))
        screen.blit(txt_MH_val, self.coo(90, 30))
        screen.blit(txt_BH_val, self.coo(90, 60))
