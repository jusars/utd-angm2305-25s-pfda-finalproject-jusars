import sys, os
import pygame
from pygame import Vector2
import random

pygame.init()

# utility
"""tldr: function to load sprites (image) and resize when needed"""
def gameImageLoad(imagefilepath, size):
        image = pygame.image.load(imagefilepath)
        image = pygame.transform.scale(image, (size[0], size[1]))
        return image

def gameWindowUpdating():
     # bg image
     SCREEN.blit(BGIMG, (0,0))

     pygame.display.update()
     
# game objects

# game settings variables
SCREENWIDTH = 2560
SCREENHEIGHT = 1440
clock = pygame.time.Clock

# pygame display window
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("legally distinct asteroids game")

# loading game assets
BGIMG = gameImageLoad('assets/space.png', (SCREENWIDTH, SCREENHEIGHT))

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

    gameWindowUpdating()
    clock.tick(60)

        