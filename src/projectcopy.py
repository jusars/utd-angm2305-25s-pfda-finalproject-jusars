import random
import math # i might want to use math
import pygame
from os.path import join

"""old code"""
class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT /2))
    
    def update(self):
        print('ship updated')
# general setup (initializing, window, etc)
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 2560, 1440 # i have to do this otherwise my monitor rejects it
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Legally Distinct Asteroids Game')
running = True
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player(all_sprites)


# importing images
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = ((WINDOW_WIDTH // 2), (WINDOW_HEIGHT // 2)))
player_direction = pygame.math.Vector2()
player_speed = 300

star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [ (random.randrange(0, WINDOW_WIDTH), random.randrange(0, WINDOW_HEIGHT)) for i in range(20)]

meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = ((WINDOW_WIDTH // 2), (WINDOW_HEIGHT //2)))

laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20,(WINDOW_HEIGHT - 20)))

while running:
    dt = clock.tick(60) / 1000
    # event loop
    # ESCAPE key to quit game
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
#        if event.type == pygame.KEYDOWN and event.key
#        if event.type == pygame.MOUSEBUTTONDOWN
#            player_rect.center = event.pos

    #player input
#     (pygame.mouse.get_pos())
    #    keys = pygame.key.get_pressed()
    #player_direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a]) or (int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT]))
    #player_direction.y = (int(keys[pygame.K_s]) - int(keys[pygame.K_w])) or (int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP]))
    #

    # player_rect.center += player_direction * player_speed * dt
    #recent_keys = pygame.key.get_just_pressed()
    #if recent_keys[pygame.K_SPACE]:
     #   print('fire laser')

    all_sprites.update()

    # drawing the game
    display_surface.fill('midnightblue')
    for pos in star_positions:
        display_surface.blit(star_surf, pos)
    
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)
    #display_surface.blit(player_surf, player_rect.topleft)
    #display_surface.blit(player.image, player.rect)
    all_sprites.draw(display_surface)

    pygame.display.update()

pygame.quit