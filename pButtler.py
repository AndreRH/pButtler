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
F_fadeIn = False
F_fadeOut = False
fadeInc = 10
fadeSpeed = 50
fadeTime = 0

# Create the two fading functions
def fadeOut():
    global F_fadeIn, F_fadeOut, fadeTime
    (F_fadeIn, F_fadeOut) = (False, True)
    fadeTime = pygame.time.get_ticks()

def fadeIn():
    global F_fadeIn, F_fadeOut, fadeTime
    (F_fadeIn, F_fadeOut) = (True, False)
    fadeTime = pygame.time.get_ticks()


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
    clock.tick(60)
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
                fadeIn()
            if event.key == pygame.K_DOWN:
                fadeOut()

    # Screensaver
    if not F_saver and t - saverTime > saverTimer:
        F_saver = True
        fadeOut()
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
    if F_fadeIn and t - fadeTime > fadeSpeed:
        a = surface.get_alpha() + fadeInc
        if a > 255:
            (a, F_fadeIn) = (255, False)
        surface.set_alpha(a)
        fadeTime = pygame.time.get_ticks()
    elif F_fadeOut and t - fadeTime > fadeSpeed:
        a = surface.get_alpha() - fadeInc
        if a < 0:
            (a, F_fadeOut) = (0, False)
        surface.set_alpha(a)
        fadeTime = pygame.time.get_ticks()

    # Update screen
    screen.blit(surface, (0, 0))
    pygame.display.flip()

# Close the windows and quit
pygame.quit()
