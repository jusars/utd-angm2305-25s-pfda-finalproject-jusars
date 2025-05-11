from pygame.math import Vector2
from utils import load_sprite

class GameObject:
    def __init__(self, position, sprite, velocity):
        sprite = pygame.Surface((50, 50))
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite[0] / 2
        self.velocity = Vector2(velocity)

    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)

    def move(self):
        self.position = self.position + self.velocity

    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius