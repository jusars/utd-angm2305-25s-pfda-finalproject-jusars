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
                AsteroidImgA[imgSize].append(gameImageLoad(f'assets/asteroids/{imgSize}/{item}', (imgSpriteSize, imgSpriteSize)))
            elif str(item)[:2] == 'a3':
                AsteroidImgB[imgSize].append(gameImageLoad(f'assets/asteroids/{imgSize}/{item}', (imgSpriteSize, imgSpriteSize)))

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

def stage_progression():
     """checks # of asteroids on screen, 
     increases stage level when no asteroids"""
     global stage
     if len(asteroidObjects) == 0:
          stage += 1
          generate_asteroids()

def generate_asteroids():
     """generates asteroids corresponding to lvl"""
     for _ in range(stage):
          asteroidObjects.append(Asteroid('large'))

def resetAfterLosingLife():
     """resetting player to mid. of screen + move
     asteroids to new locations after player is hit."""
     player.pos = (screen_width // 2, screen_height // 2)
     player.direction = Vector2(0, -1)
     player.velocity = Vector2()
     playerBullets.clear()
     if not gameover:
          for index, asteroidObject in enumerate(asteroidObjects):
               asteroidObject.pos = generate_random_location()
          pygame.time.wait(3000)
     else:
          asteroidObjects.clear()

def textScreen(message):
     """ putting text on the screen"""
     font = pygame.font.SysFont('comicsans', 40)
     displayText = font.render(message, 1, (255, 255, 255))
     return displayText

def gameWindowUpdating():
     # drawing bg image to screen
     GAMESCREEN.blit(bg_img, (0,0))

     if not gameover:
          # drawing bullets to screen
          for bullet in playerBullets:
               bullet.move()
               bullet.draw(GAMESCREEN)

          for asteroidObject in asteroidObjects:
               asteroidObject.draw(GAMESCREEN)
               asteroidObject._animate_image()

     # drawing player image on screen
     player.draw(GAMESCREEN)

     # text display for score, lives, top score, stage, etc
     playerLives = textScreen(f'Player Lives: {str(lives)}')
     GAMESCREEN.blit(playerLives, (25, 25))
     stage_text = textScreen(f'STAGE: {str(stage)}')
     GAMESCREEN.blit(stage_text, (25, 25 + playerLives.get_height() + 10))
     score_text = textScreen(f'SCORE: {str(score)}')
     GAMESCREEN.blit(score_text, (screen_width - 25 - score_text.get_width(), 25))
     topscore_text = textScreen(f'TOP SCORE: {str(topscore)}')
     GAMESCREEN.blit(topscore_text, (screen_width - 25 - topscore_text.get_width(),
                                      25 + topscore_text.get_height() + 10)) 
     # percentage bar for asteroids destroyed

     asteroidsRectangleWidth = screen_width - 100 - score_text.get_width() - playerLives.get_width()
     pygame.draw.rect(GAMESCREEN, [173, 36, 105], [25 + playerLives.get_width() + 25,
                                                    25, asteroidsRectangleWidth,
                                                      playerLives.get_height()])
     numAsteroids = calculateTotalAsteroids()
     
     
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
          self.imgRect = pygame.rect.Rect(self.imgRect.x, self.imgRect.y,
                                          self.width, self.height)
          self.direction = Vector2(random.randrange(-100, 100)/100,
                                   random.randrange(-100, 100)/100)
          self.speed = random.randrange(3, 6)
          self.imgInd = 0
          self.animate_speed = random.randrange(3, 7)
          # tldr: large asteroid: 3 hits, medium : 2 hits, small: 1 hit
          self.health = 3 if self.size == 'large' else 2 if self.size == 'medium' else 1
          self.score = 10 if self.size == 'large' else 20 if self.size == 'medium' else 50
     
     def _generate_random_image_set(self):
          if self.size == 'large':
               imgSet = random.choice([AsteroidImgA, AsteroidImgB])
          return imgSet
     
     def accelerate(self):
          # increases speed of asteroid object
          self.velocity = self.direction * self.speed

     def _animate_image(self):
          """cycles thru numbered pngs. at random animation speeds"""
          self.imgInd += 1
          if self.imgInd % self.animate_speed == 0:
               self.imgIndex = self.imgInd // self.animate_speed
          if self.imgIndex == len(self.imgSet[self.size]) - 1:
               self.imgInd = 0
               self.imgIndex = 0
          self.img = self.imgSet[self.size][self.imgIndex]

     def move (self):
          super().move() # reusing 'move' under player class lol
          self.accelerate() # acceleration exclusive to asteroids

# game settings variables
clock = pygame.time.Clock()
screen_width = 2560
screen_height = 1440
object_rotation_speed = 2
object_speed = 0.25
stage = 0
lives = 3
gameover = False
score = 0
topscore = None

# pygame display window
GAMESCREEN = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("legally distinct asteroids game")


# loading game assets
bg_img = gameImageLoad('assets/space.png', (screen_width, screen_height))
player_img = gameImageLoad('assets/spaceship.png', (75, 75))
AsteroidImgA = {'large': [], 'medium': [], 'small': []}
AsteroidImgB = {'large': [], 'medium': [], 'small': []}

# one off functions (loading gameobjects, etc)
    # loading asteroids
asteroidImageLoading()
     # calling the player
player = Player(((screen_width // 2), (screen_height // 2)))


# game object lists
playerBullets = []
asteroidObjects = []

"""MAIN GAME LOOP"""
running = True
while running:

    if not gameover:

     stage_progression()

     # update game object movements
     player.move()
     for index, bullet in enumerate(playerBullets):
          bullet.move()

          # check to see if bullet is offscreen (and kills it)
          if bullet.check_if_offscreen():
               del playerBullets[index]

     for ind, asteroidObject in enumerate(asteroidObjects):
               asteroidObject.move()

               for index, bullet in enumerate(playerBullets):
                    if bullet.bulletRect.colliderect(asteroidObject.imgRect):
                         asteroidObject.health -= 1
                         score += asteroidObject.score
                         if asteroidObject.health == 0:
                              if asteroidObject.size == 'large':
                                   asteroidObjects.append(Asteroid('medium', asteroidObject.pos,
                                                                 asteroidObject.imgSet))
                                   asteroidObjects.append(Asteroid('medium', asteroidObject.pos,
                                                                 asteroidObject.imgSet))
                              elif asteroidObject.size == 'medium':
                                   asteroidObjects.append(Asteroid('small', asteroidObject.pos,
                                                                 asteroidObject.imgSet))
                                   asteroidObjects.append(Asteroid('small', asteroidObject.pos,
                                                                 asteroidObject.imgSet))
                              del asteroidObjects[ind]
                         del playerBullets[index]
                         break
               if asteroidObject.imgRect.colliderect(player.imgRect):
                    lives -= 1
                    if lives <= 0:
                         gameover = True
                    else:
                         resetAfterLosingLife()
                         del asteroidObjects[ind]
                         break
                    break

    # one time press inputs
    for event in pygame.event.get():
          if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            running = False
          if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
               playerBullets.append(Bullet(player.pos, player.direction))
          if gameover:
               if event.key == pygame.K_TAB:
                    resetAfterLosingLife()
                    stage = 1
                    lives = 3
                    generate_asteroids()
                    gameover = False

    # handling inputs that are held down
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
         player.rotation(-2.5)
    elif keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
         player.rotation(2.5)
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
         player.accelerate()

    gameWindowUpdating()
    clock.tick(60)

pygame.quit()
sys.exit()
        