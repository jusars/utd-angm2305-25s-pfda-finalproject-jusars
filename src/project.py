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
     # bg image displayed on screen
     GAMESCREEN.blit(bg_img, (0,0))

     for bullet in playerBullets: # drawing bullets to screen
          bullet.move()
          bullet.draw(GAMESCREEN)

     # drawing player image on screen
     player.draw(GAMESCREEN)

     pygame.display.update()
     
# game objects / major classes :)
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
    
      def accelerate(self):
          """increasing speed of player object"""
          self.velocity += self.direction * self.speed

      def rotation (self, rotation=2):
          """accepting input for rotating player object"""
          angle = self.rotation_speed * rotation
          self.direction.rotate_ip(angle)

      def _wrap_to_screen(self, position):
           # wrapping around screen so player doesn't get lost perpetually
           self.x, self.y = position
           return Vector2(self.x % screen_width, self.y % screen_height)

      def move(self):
          """updating player position"""
          self.pos += self.velocity
          self.pos = self._wrap_to_screen(self.pos)
          self.imgRect.x, self.imgRect.y = (self.pos[0] - self.width //2,
                                             self.pos[1] - self.height//2)
          self.velocity *= 0.99 # adding friction (sort of)

      def draw(self, window):
        """tldr: alters/ accepts image rotation and latest coordinates, then blits"""
        # letting those asteroids fly diagonally instead of just left and right
        angle = self.direction.angle_to(Vector2(0, -1))
        rotated_img = pygame.transform.rotozoom(self.img, angle, 1.0)
        rotated_img_size = Vector2(rotated_img.get_size())
        blit_pos = self.pos - rotated_img_size * 0.5
        window.blit(rotated_img, blit_pos)
        pygame.draw.rect(window, [255, 255, 255], [self.imgRect.x, self.imgRect.y,
                                                   self.width, self.height], 1)

class Bullet:
     def __init__(self, coords, direction):
          self.width = 4
          self.height = 4
          self.pos = Vector2(coords[0], coords[1])
          self.direction = Vector2(direction[0], direction[1])
          self.velocity = Vector2()
          self.speed = 10

     def move(self):
          """updating bullet position"""
          self.pos += (self.direction + self.speed)

     def draw(self, window):
          """draws bullet to screen"""
          pygame.draw.rect(window, (255, 255, 255), [self.pos[0], self.pos[1],
                                                 self.width, self.height])
          self.bulletRect = pygame.rect.Rect(int(self.pos[0], int(self.pos[1]),
                                             self.width, self.height))

# game settings variables
clock = pygame.time.Clock()
screen_width = 2560
screen_height = 1440
object_rotation_speed = 2
object_speed = 0.25

# pygame display window
GAMESCREEN = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("legally distinct asteroids game")

# loading game assets
bg_img = gameImageLoad('assets/space.png', (screen_width, screen_height))
player_img = gameImageLoad('assets/spaceship.png', (75, 75))

# one off functions (loading gameobjects, etc)
    # calling player
player = Player(((screen_width // 2), (screen_height // 2)))
# game object lists
playerBullets = []
# main game loop
running = True
while running:

    # update game object movements
    player.move()
for index, bullet in enumerate(playerBullets):
    bullet.move()

    # exit functionality
    for event in pygame.event.get():
          if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            running = False
          if event.key == pygame.K_SPACE:
               playerBullets.append(Bullet(player.pos,))

    # handling input
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
         player.rotation(-1)
    elif keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
         player.rotation(1)
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
         player.accelerate()

    gameWindowUpdating()
    clock.tick(60)

        