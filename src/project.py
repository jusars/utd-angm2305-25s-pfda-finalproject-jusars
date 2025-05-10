import random
import math # i might want to use math
import pygame
from os.path import join

"""starting from almost scratch unfortunately (referring to a different tutorial),
I got way too lost :("""

class AsteroidsGame:
    def __init__(self):
            self._init_pygame()
            self.screen = pygame.display.set_mode((2560, 1440))

    def game_loop(self):
        while True:
            self._handle_input()
            self._game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Legally Distinct Asteroids Game")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
            event.type ==pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                pygame.quit

    def _game_logic(self):
        pass

    def _draw(self):
        self.screen.fill((0, 0, 255))
        pygame.display.flip()