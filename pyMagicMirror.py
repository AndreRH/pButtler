#!/usr/bin/python
#-*- coding:utf-8 -*-

"""
------------ pyMagicMirror --
-- by antoine@2ohm.fr --
-- by nerv@dawncrow.de --
------------------------
"""

import pygame
import time
import os

# Import widgets
from widgets.w_DateTime import *
#from widgets.w_Roles import *
from widgets.w_Maxim import *
#from widgets.w_Calendar import *

# Init the pygame
pygame.init()

# Set the screen to fullscreen
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

# Init the main surface
surface = pygame.Surface(screen.get_size())

# Init widgets
widgets = {
    "w_DateTime": w_DateTime(pygame, screen),
    #"w_Roles": w_Roles(pygame, screen),
    "w_Maxim": w_Maxim(pygame, screen),
    #"w_Calendar": w_Calendar(pygame, screen)
    }

# Main loop
# Loop until the user clicks the close button
mustQuit = False

# Used to set the screen update rate
clock = pygame.time.Clock()

# Init the screensaver
saverTime = pygame.time.get_ticks()

while not mustQuit:
    # Set the frame rate
    tt = clock.tick(60)
    t = pygame.time.get_ticks()

    # Solve events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mustQuit = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                mustQuit = True

    # Clear the screen to black
    screen.fill(c_BLACK)
    surface.fill(c_BLACK)

    # Update widgets
    for widget in widgets.values():
        widget.update(surface, t)

    # Update screen
    screen.blit(surface, (0, 0))
    pygame.display.flip()

# Close the windows and quit
pygame.quit()
