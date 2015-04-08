#!/usr/bin/python
#-*- coding:utf-8 -*-

"""
------------ pButtler --
-- by antoine@2ohm.fr --
------------------------
"""

import pygame
import time

# Init the pygame
pygame.init()

## CSS
# Define some fonts
font_time = pygame.font.SysFont(
        'Helvetica', 75, bold=False, italic=False)
font_date = pygame.font.SysFont(
        'Helvetica', 20, bold=False, italic=False)

# Define some colors
c_BLACK = (0, 0, 0)
c_WHITE = (221, 221, 221)

# Set width and height
size = (700, 500)
#screen = pygame.display.set_mode(size)
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

pygame.display.set_caption("buttler")

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

    # Display time
    str_time = time.strftime("%H:%M:%S")
    str_date = time.strftime("%A %d %B %Y")

    txt_time = font_time.render(str_time, True, c_WHITE)
    txt_date = font_date.render(str_date, True, c_WHITE)
    screen.blit(txt_time, [150, 150])
    screen.blit(txt_date, [200, 225])

    # Update screen
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Close the windows and quit
pygame.quit()
