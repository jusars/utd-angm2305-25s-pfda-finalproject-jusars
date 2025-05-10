import random
import math # i might want to use math
import pygame
from os.path import join

"""starting from almost scratch unfortunately (referring to a different tutorial),
I got way too lost :("""

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 2560, 1440 # i have to do this otherwise my monitor rejects it
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Legally Distinct Asteroids Game')

    pygame.display.update()


pygame.quit
def main():
    pygame.init()
    pygame.display.set_caption("Legally Distinct Asteroids Game")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (2560, 1440)
    screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
    rain = Rain(resolution)
    running = True
    while running:
        # EVENT LOOP
        for event in pygame.event.get():
            # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE
            
            if event.type == pygame.QUIT or (
            event.type ==pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                running = False
        # TODO: some game logic
        rain.update(dt)
        # RENDER AND DISPLAY
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        rain.draw(screen)
        pygame.display.flip()
        # print(particle.age)
        dt = clock.tick(20)
    pygame.quit()