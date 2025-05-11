import sys, os
import pygame
from pygame import Vector2
import random

pygame.init()

# utility

# game objects

# game settings variables
SCREENWIDTH = 2560
SCREENHEIGHT = 1440
# pygame display window
SCREEN = pygame.display.set_mode(SCREENWIDTH, SCREENHEIGHT)
pygame.display.set_caption("legally distinct asteroids game")
# loading game assets

# one off functions (loading gameobjects, etc)

# game object lists

# main game loop
RUNGAME = True
while RUNGAME:

    # exit functionality
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            RUNGAME = False

        