import random
import math # i might want to use math
import pygame
from os.path import join

# general setup (initializing, window, etc)
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Legally Distinct Asteroids Game')
running = True

# importing images
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
while running:
    # event loop
    # ESCAPE key to quit game
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        

    # drawing the game
    display_surface.fill('midnightblue')
    x += 0.1
    display_surface.blit(player_surf, (x, 150))
    pygame.display.update()

pygame.quit