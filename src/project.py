import sys, os
import pygame
from pygame import Vector2
import random

pygame.init()

"""utility functions"""
# tldr: function to load sprites (image) and resize when needed
def gameImageLoad(imagefilepath, size):
        image = pygame.image.load(imagefilepath)
        image = pygame.transform.scale(image, (size[0], size[1]))
        return image

def asteroidImageLoading():
     # function for loading all the asteroid images + resize when needed
     large = 200
     medium =  125
     small = 75
     for imgSize in ['large', 'medium', 'small']:
          if imgSize == 'large':
               imgSpriteSize = large
          elif imgSize == 'medium':
               imgSpriteSize = medium
          else:
               imgSpriteSize = small
          for item in os.listdir(f'assets/asteroids/{imgSize}'):
               if str(item)[:2] == 'a1':
                    AsteroidImgA[imgSize].append(gameImageLoad
                                                 (f'assets/asteroids/{imgSize}/{item}',
                                                               (imgSpriteSize, imgSpriteSize)))
          for item in os.listdir(f'assets/asteroids/{imgSize}'):
               if str(item)[:2] == 'a3':
                    AsteroidImgA[imgSize].append(gameImageLoad
                                                 (f'assets/asteroids/{imgSize}/{item}',
                                                               (imgSpriteSize, imgSpriteSize)))

def generate_random_location():
     """generating random spawn locations for asteroids
     a certain distance away from player char"""
     playerPosX, playerPosY = player.pos
     validLocation = False
     while not validLocation:
          asteroidPosX = random.randrange(0, screen_width)
          asteroidPosY = random.randrange(0, screen_height)
          asteroidLocation = Vector2(asteroidPosX, asteroidPosY)
          if asteroidLocation.distance_to(player.pos) >= 100:
               validLocation = True
          else:
               continue
     return asteroidLocation

def gameWindowUpdating():
     # drawing bg image to screen
     GAMESCREEN.blit(bg_img, (0,0))

     # drawing bullets to screen
     for bullet in playerBullets:
          bullet.move()
          bullet.draw(GAMESCREEN)

     # drawing player image on screen
     player.draw(GAMESCREEN)

     pygame.display.update()
     
"""game objects/ classes"""
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
          # increasing speed of player object
          self.velocity += self.direction * self.speed

      def rotation (self, rotation=2):
          # accepting input for rotating player object
          angle = self.rotation_speed * rotation
          self.direction.rotate_ip(angle)

      def _wrap_to_screen(self, position):
           # wrapping around screen so player doesn't get lost perpetually
           self.x, self.y = position
           return Vector2(self.x % screen_width, self.y % screen_height)

      def move(self):
          # updating player position
          self.pos += self.velocity
          self.pos = self._wrap_to_screen(self.pos)
          self.imgRect.x, self.imgRect.y = (self.pos[0] - self.width //2,
                                             self.pos[1] - self.height//2)
          self.velocity *= 0.99 # adding friction (sort of)

      def draw(self, window):
        """tldr: alters/ accepts image rotation and latest coordinates, then blits"""
        # letting objects fly diagonally instead of just left and right
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
          self.pos += (self.direction * self.speed)

     def check_if_offscreen(self):
          """checking if bullets are offscreen (to be killed later)"""
          if (self.pos[0] < 0 or self.pos[0] > screen_width or
               self.pos[1] < 0 or self.pos[1] > screen_height):
               return True
          
     def draw(self, window):
          """draws bullet to screen"""
          pygame.draw.rect(window, (255, 255, 255), [self.pos[0], self.pos[1], 
                                                     self.width, self.height])
          self.bulletRect = pygame.rect.Rect(int(self.pos[0]), int(self.pos[1]),
                                                     self.width, self.height)


class Asteroid(Player):
     def __init__(self, size, coords=(0, 0), imgSet=None):
          super().__init__(coords)
          self.size = size
          self.x, self.y = (generate_random_location()
                             if self.size == 'large'else coords)
          self.imgSet = (self._generate_random_image_set() if not imgSet
                          else imgSet)
          self.imgIndex = 0
          self.img = self.imgSet[self.size][self.imgIndex]
          self.width = self.img.get_width() // 2
          self.height = self.img.get_height() // 2
          self.imgRect.x = self.x - self.width // 2
          self.imgRect.y = self.y - self.height // 2
          self.imgRect = pygame.rext.Rect(self.imgRect.x, self.imgRect.y,
                                          self.width, self.height)
          self.direction = Vector2(random.randrange(-100, 100)/100,
                                   random.randrange(-100, 100)/100)
          self.speed = random.randrange(3, 6)
     
     def _generate_random_image_set(self):
          if self.size == 'large':
               imgSet = random.choice([AsteroidImgA])
          return imgSet
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
AsteroidImgA = {'large': [], 'medium': [], 'small': []}


# one off functions (loading gameobjects, etc)
    # loading asteroids
asteroidImageLoading()
     # calling the player
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

         # check to see if bullet is offscreen (and kills it)
         if bullet.check_if_offscreen():
              del playerBullets[index]

    # exit functionality + other inputs
    for event in pygame.event.get():
          if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            running = False
          if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
               playerBullets.append(Bullet(player.pos, player.direction))

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

pygame.quit()
sys.exit()
        