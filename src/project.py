import random
import math # i might want to use math
import pygame
from os.path import join

# general setup (initializing, window, etc)
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 2560, 1440 # i have to do this otherwise my monitor rejects it
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Legally Distinct Asteroids Game')
running = True
clock = pygame.time.Clock()

# importing images
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = ((WINDOW_WIDTH // 2), (WINDOW_HEIGHT // 2)))
player_direction = -1

star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [ (random.randrange(0, WINDOW_WIDTH), random.randrange(0, WINDOW_HEIGHT)) for i in range(20)]

meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = ((WINDOW_WIDTH // 2), (WINDOW_HEIGHT //2)))

laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20,(WINDOW_HEIGHT - 20)))

while running:
    clock.tick(24) #24 fps :)
    # event loop
    # ESCAPE key to quit game
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # drawing the game
    display_surface.fill('midnightblue')
    for pos in star_positions:
        display_surface.blit(star_surf, pos)
    
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)

    # player movement
    player_rect.x += player_direction * 1
    if player_rect.right > WINDOW_WIDTH or player_rect.left <0:
        player_direction *= -1
    display_surface.blit(player_surf, player_rect.topleft)

    pygame.display.update()

pygame.quit