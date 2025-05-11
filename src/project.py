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
     # bg image displayed in game
     screen.blit(bg_img, (0,0))

     # drawing player image in game
     player.draw(screen)

     pygame.display.update()
     
# game objects
class Player:
     def __init__(self, coords):
          self.img = player_img
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

def draw(self, window):
     """tldr: alters/ accepts image rotation and latest coordinates, then blits"""
     # letting those asteroids fly diagonally instead of just left and right
     angle = self.direction.angle.to(Vector2(0, -1))
     rotated_img = pygame.Transform.rotozoom(self.img, angle, 1.0)
     rotated_img_size = Vector2(rotated_img.get_size())
     blit_pos = self.pos - rotated_img_size * 0.5
     window.blit(rotated_img, blit_pos)

# game settings variables
clock = pygame.time.Clock
screen_width = 2560
screen_height = 1440
object_rotation_speed = 2
object_speed = 0.25

# pygame display window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("legally distinct asteroids game")

# loading game assets
bg_img = gameImageLoad('assets/space.png', (screen_width, screen_height))
player_img = gameImageLoad('assets/spaceship.png', (75, 75))

# one off functions (loading gameobjects, etc)
    # calling player
player = Player(((screen_width // 2), (screen_height // 2)))
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

        