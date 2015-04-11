# -*- coding:utf-8 -*-

import time
import datetime
import caldav

from widgets.widget import *

class w_Calendar(widget):
    """Widget - Calendar
    Display the shared calendar.
    """

    def __init__(self, game, screen):
        """Initialize the widget.
        """
        widget.__init__(self, game, screen)

        # Update needed properties
        self.name = "w_Calendar"
        self.x = self.coo_right(400)
        self.y = 180

        # Define custom properties
        # Caldav properties
        self.cal_url = "https://leCortho:ivrycestjoli@owncloud.2ohm.fr/remote.php/caldav/"
        self.cal_client = caldav.DAVClient(
                self.cal_url, ssl_verify_cert=False)
        self.cal_cal = self.cal_client.principal().calendars()[0]

        # Timing properties
        self.lastUpdate = 0
        self.updateRate = 5*60*1000

        # Calendar properties
        self.events = []
        self.delta_days = 31

        # Define some local properties
        self.days_french = ["lundi", "mardi", "mercredi", "jeudi",
                    "vendredi", "samedi", "dimanche"]
        self.months_french = ["janvier", "février", "mars", "avril",
                "mai", "juin", "juillet", "aout", "septembre",
                "octobre", "novembre", "décembre"]

        # Define some font
        self.font = self.game.font.SysFont(
                'Helvetica', 18, bold=False, italic=False)

        # Update the event list
        self.updateEvents()

    def updateEvents(self):
        """Update the event list.
        """
        # Update calendar data
        d_start = datetime.datetime.today()
        d_end = d_start + datetime.timedelta(self.delta_days)
        results = self.cal_cal.date_search(d_start, d_end)

        # Flush the events dict
        self.events = []
        # Add each events
        for event in results:
            # Format the title of the event
            str_title = event.instance.vevent.summary.value
            if len(str_title) > 20:
                str_title = str_title[:17] + "..."
            # Format the date of the event
            vdate = event.instance.vevent.dtstart.value
            d = datetime.datetime.strptime(
                    vdate.strftime("%d %m %Y"), "%d %m %Y")
            str_date = "%s %d %s" % (
                self.days_french[d.weekday()],
                d.day,
                self.months_french[d.month -1])
            # Format the date gap
            gap = 1 + (d - d_start).days
            # Save the event
            self.events.append((str_title, str_date, gap))

    def update(self, screen, t):
        if t - self.lastUpdate > self.updateRate:
            # Update the lastUpdate timer
            self.lastUpdate = t
            # Update events
            self.updateEvents()

        # Init the y-index
        y = 0
        for (title, date, gap) in sorted(self.events,
                key=lambda e: e[2]):
            # Compute new color in function of the gap
            c_title = tuple(
                [int(c*(self.delta_days - gap)/self.delta_days) for c in c_WHITE])
            c_date = tuple(
                [int(c*(1 - gap/self.delta_days)) for c in c_GRAY])

            txt_title = self.font.render(title, True, c_title)
            txt_date = self.font.render(date, True, c_date)

            screen.blit(txt_title, self.coo(0, y))
            screen.blit(txt_date, self.coo(250, y))

            # Update the y-index
            y += 25
