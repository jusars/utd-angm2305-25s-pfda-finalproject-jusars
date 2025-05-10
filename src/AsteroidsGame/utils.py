# tldr: image loading functions that are reusable. I THINK.
from pygame.image import load

def load_sprite(name, with_alpha=True):
    path =f"src/sprites/{name}.png"
    loaded_sprite = load(path)

    if with_alpha:
        return loaded_sprite.convert_alpha
    else:
        return loaded_sprite.convert()