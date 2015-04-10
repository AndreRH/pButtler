#!/usr/bin/python
#-*- coding:utf-8 -*-

"""
------------ pButtler --
-- by antoine@2ohm.fr --
------------------------
"""

import pygame
import time

# Import widgets
from widgets.w_DateTime import *

# Init the pygame
pygame.init()

## Set width and height
#size = (700, 500)
#screen = pygame.display.set_mode(size)

# Set the screen to fulscreen
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

pygame.display.set_caption("buttler")

# Init widgets
widgets = {"w_DateTime": w_DateTime(pygame)}

# Main loop
# Loop until the user clicks the close button
mustQuit = False

# Used to set the screen update rate
clock = pygame.time.Clock()

while not mustQuit:
    # Solve events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mustQuit = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                mustQuit = True
    
    # --- Dashboard logic

    # --- Drawing code
    # Clear the screen to black
    screen.fill(c_BLACK)

    # Update widgets
    for widget in widgets.values():
        widget.update(screen)

    # Update screen
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Close the windows and quit
pygame.quit()
