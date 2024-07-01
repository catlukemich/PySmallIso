from functools import cmp_to_key

from .CullingGrid import CullingGrid


class Scene:
    def __init__(self, cell_size=20):
        self.cell_size = cell_size
        self.sprites = []
        self.layers = []
        self.grid = CullingGrid(cell_size)

    def add_sprite(self, sprite):
        location = sprite.get_location()
        self.grid.add_sprite(sprite, location)
        sprite.set_scene(self)

    def remove_sprite(self, sprite):
        location = sprite.get_location()
        self.grid.remove_sprite(sprite, location)
        sprite.set_scene(None)

    def get_cell_size(self):
        return self.cell_size

    def get_grid(self):
        return self.grid

    def update_sprite_location(self, sprite, old_location, new_location):
        self.grid.update_sprite_location(sprite, old_location, new_location)


