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

# plain surface (not having this broke my code?)
surf = pygame.Surface((100,200))
surf.fill('gray')
x = 100

# importing images
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = ((WINDOW_WIDTH // 2), (WINDOW_HEIGHT // 2)))

star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [ (random.randrange(0, WINDOW_WIDTH), random.randrange(0, WINDOW_HEIGHT)) for i in range(20)]

while running:
    # event loop
    # ESCAPE key to quit game
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        

    # drawing the game
    display_surface.fill('midnightblue')

    for pos in star_positions:
        display_surface.blit(star_surf, pos)
    display_surface.blit(player_surf, player_rect)
    pygame.display.update()
pygame.quit