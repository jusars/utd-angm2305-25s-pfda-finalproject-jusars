import random
import math # i might want to use math
import pygame

# general setup (initializing, window, etc)
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1920, 1080
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Legally Distinct Asteroids Game')
running = True

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # drawing the game
    display_surface.fill('midnightblue')
    pygame.display.update()

pygame.quit