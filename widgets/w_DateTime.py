# -*- coding:utf-8 -*-

import os, time

from widgets.widget import *

class w_DateTime(widget):
    """Widget - Date & Time
    Display the date and the local time.
    """

    def __init__(self, game, screen):
        """Initialize the widget.
        """
        widget.__init__(self, game, screen)

        # Update needed properties
        self.name = "w_DateTime"
        self.x = 100
        self.y = 50

        # Define some font
        self.font_hour = self.game.font.SysFont(
                'Helvetica', 75, bold=True, italic=False)
        self.font_minute = self.game.font.SysFont(
                'Helvetica', 75, bold=False, italic=False)
        self.font_date = self.game.font.SysFont(
                'Helvetica', 20, bold=False, italic=False)

        # Define some local properties
        self.days_french = ["lundi", "mardi", "mercredi", "jeudi",
                    "vendredi", "samedi", "dimanche"]
        self.months_french = ["janvier", "février", "mars", "avril",
                "mai", "juin", "juillet", "aout", "septembre",
                "octobre", "novembre", "décembre"]
        self.days_german = ["Montag", "Dienstag", "Mittwoch", "Donnerstag",
                    "Freitag", "Samstag", "Sonntag"]
        self.days_german_short = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
        self.months_german = ["nuhl", "Januar", "Februar", "März", "April",
                "Mai", "Juni", "Juli", "August", "September",
                "Oktober", "November", "Dezember"]

        os.environ['TZ'] = 'Europe/Berlin'
        time.tzset()

    def update(self, screen, t):
        lt = time.localtime()
        str_hour = time.strftime("%H")
        str_minute = time.strftime("%M")
        str_date = "%s. %d. %s %d" % (
                self.days_german_short[lt.tm_wday],
                lt.tm_mday,
                self.months_german[lt.tm_mon],
                lt.tm_year)

        txt_hour = self.font_hour.render(str_hour, True, c_WHITE)
        txt_minute = self.font_minute.render(str_minute, True, c_WHITE)
        txt_date = self.font_date.render(str_date, True, c_WHITE)

        screen.blit(txt_hour, self.coo(0, 0))
        screen.blit(txt_minute, self.coo(0, txt_hour.get_height() - 15))
        screen.blit(txt_date, self.coo(0, txt_hour.get_height() + txt_minute.get_height() - 20))
