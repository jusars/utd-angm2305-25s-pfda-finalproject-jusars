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
class Player:
     def __init__(self, coords):
          self.img = PlayerImg
          self.imgRect = self.img.get_rect()
          self.x, self.y = coords
          self.width = self.img.get_width()
          self.height = self.img.get_height()
          # centering rectangle to image
          self.imgRect.x = self.x - self.width // 2
          self.imgRect.y = self.y - self.height // 2
          self.pos = Vector2(self.imgRect.x, self.imgRect.y)
          self.direction = Vector2(0, -1)
          self.velocity = Vector2()
          self.rotation_speed = object_rotation_speed
          self.speed = object_speed

# game settings variables
clock = pygame.time.Clock
SCREENWIDTH = 2560
SCREENHEIGHT = 1440
object_rotation_speed = 2
object_speed = 0.25

# pygame display window
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("legally distinct asteroids game")

# loading game assets
BGIMG = gameImageLoad('assets/space.png', (SCREENWIDTH, SCREENHEIGHT))
PlayerImg = gameImageLoad('assets/spaceship.png', (75, 75))

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

        