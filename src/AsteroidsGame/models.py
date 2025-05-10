from pygame.math import Vector2

class GameObject:
    def __init__(self, position, sprite, velocity)
        self.position = Vector2(position)
        self.sprite = spriteself.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)