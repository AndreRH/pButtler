# -*- coding:utf-8 -*-

import time

from widgets.widget import *

class w_DateTime(widget):
    """Widget - Date & Time
    Display the date and the local time.
    """

    def __init__(self, game):
        """Initialize the widget.
        """
        widget.__init__(self, game)

        # Update needed properties
        self.name = "w_DateTime"
        self.x = 100
        self.y = 50

        # Define some font
        self.font_time = self.game.font.SysFont(
                'Helvetica', 75, bold=False, italic=False)
        self.font_date = self.game.font.SysFont(
                'Helvetica', 20, bold=False, italic=False)

        # Define some local properties
        self.days_french = ["lundi", "mardi", "mercredi", "jeudi",
                    "vendredi", "samedi", "dimanche"]
        self.months_french = ["janvier", "février", "mars", "avril",
                "mai", "juin", "juillet", "aout", "septembre",
                "octobre", "novembre", "décembre"]

    def update(self, screen):
        t = time.localtime()
        str_time = time.strftime("%H:%M:%S")
        str_date = "%s %d %s %d" % (
                self.days_french[t.tm_wday],
                t.tm_mday,
                self.months_french[t.tm_mon],
                t.tm_year)

        txt_time = self.font_time.render(str_time, True, c_WHITE)
        txt_date = self.font_date.render(str_date, True, c_WHITE)

        screen.blit(txt_time, self.coo(0, 0))
        screen.blit(txt_date, self.coo(50, 90))
