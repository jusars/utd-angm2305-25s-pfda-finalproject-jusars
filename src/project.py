import random
import math # i might want to use math
import pygame
from os.path import join

"""starting from almost scratch unfortunately (referring to a different tutorial),
I got way too lost :("""


def main():
    pygame.init()
    pygame.display.set_caption("Legally Distinct Asteroids Game")
    resolution = (2560, 1440)
    screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
    
    pygame.quit()