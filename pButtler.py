#!/usr/bin/python
#-*- coding:utf-8 -*-

"""
------------ pButtler --
-- by antoine@2ohm.fr --
------------------------
"""

import pygame
import time
import os

# Import widgets
from widgets.w_DateTime import *
from widgets.w_Roles import *
from widgets.w_Maxim import *

# Init the pygame
pygame.init()

# Set the screen to fullscreen
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

pygame.display.set_caption("buttler")

# Init the main surface
surface = pygame.Surface(screen.get_size())
surface.set_alpha(255)

# Init the fading properties
(FADE_IN, FADE_OUT, FADE_STOP) = (1, -1, 0)
fadeDir = FADE_STOP
fadeSpeed = 5

# Define custom events
FADING = pygame.USEREVENT +1
event_fadeIn = pygame.event.Event(FADING, dir = FADE_IN)
event_fadeOut = pygame.event.Event(FADING, dir = FADE_OUT)
event_fadeStop = pygame.event.Event(FADING, dir = FADE_STOP)

# Init the screensaver properties
F_saver = False     # Set to True when the screensaver is turned on
saverTimer = 60000   # Time without activity to trigger the screensaver
saverTime = 0       # Time of the last activity

# Init widgets
widgets = {
    "w_DateTime": w_DateTime(pygame),
    "w_Roles": w_Roles(pygame),
    "w_Maxim": w_Maxim(pygame)
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
            # Update the screensaver activity tracker
            saverTime = pygame.time.get_ticks()
            F_saver = False

            if event.key == pygame.K_ESCAPE:
                mustQuit = True
            if event.key == pygame.K_UP:
                pygame.event.post(event_fadeIn)
            if event.key == pygame.K_DOWN:
                pygame.event.post(event_fadeOut)

        # Solve fading events
        if event.type == FADING:
            fadeDir = event.dir

    # Screensaver
    if not F_saver and t - saverTime > saverTimer:
        F_saver = True
        pygame.event.post(event_fadeOut)
    if F_saver and surface.get_alpha() == 0:
        os.system("xset dpms force off")

    
    # --- Drawing code
    # Clear the screen to black
    screen.fill(c_BLACK)
    surface.fill(c_BLACK)

    # Update widgets
    for widget in widgets.values():
        widget.update(surface)

    # Update the fading if necessary
    if fadeDir != FADE_STOP:
        a = surface.get_alpha() + fadeDir*tt/fadeSpeed
        if a < 0:
            a = 0
            fadeDir = FADE_STOP
        elif a > 255:
            a = 255
            fadeDir = FADE_STOP
        surface.set_alpha(a)

    # Update screen
    screen.blit(surface, (0, 0))
    pygame.display.flip()

# Close the windows and quit
pygame.quit()
