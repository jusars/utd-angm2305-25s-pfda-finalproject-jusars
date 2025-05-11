import sys, os
import pygame
from pygame import Vector2
import random

pygame.init()

# utility
"""tldr: function to load sprites (image) and resize when needed"""
def gameimageload(imagefilepath, size):
        image = pygame.image.load(imagefilepath)
        image = pygame.transform.scale(image, (size[0], size[1]))
        return image

# game objects

# game settings variables
SCREENWIDTH = 2560
SCREENHEIGHT = 1440
# pygame display window
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("legally distinct asteroids game")
iconImg = gameimageload('assets/spaceship.png', (20, 20))
iconImg = pygame.transform.rotate(iconImg, -90)
pygame.display.set_icon(iconImg)

# loading game assets

# one off functions (loading gameobjects, etc)

# game object lists

# main game loop
running = True
while running:

    # exit functionality
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            running = False

        