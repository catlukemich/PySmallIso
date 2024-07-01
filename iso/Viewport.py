from .Rectangle import Rectangle
from .Vector2D import *
from .Vector3D import *

from .Defaults import Defaults


class Viewport:

    def __init__(self, screen, scene):
        # The screen and scene instances to use when rendering:
        self.screen = screen
        self.scene = scene

        # The tile width and height in pixels.
        # Modify this values if you want tiles to be in different size.
        defaults = Defaults.get()
        self.tile_width = defaults.tile_width
        self.tile_height = defaults.tile_height
        self.culling_strategy = defaults.culling_strategy
        self.sorting_strategy = defaults.sorting_strategy

        self.center = Vector3D(0, 0)
        self.visible = []
       

    def draw(self):
        ''' Perform drawing of the viewport '''
        # Cull and sort the geometry:
        self.visible = self.culling_strategy.cull(self.screen, self.scene, self)
        self.sorting_strategy.sort_sprites(self.visible)

        # Draw the sprites:
        for sprite in self.visible:
            sprite.draw(self, self.screen)


    def get_center(self):
        return Vector3D(self.center.x, self.center.y, 0)

    def set_center(self, center):
        self.center = center

    def set_culling_strategy(self, strategy):
        self.culling_strategy = strategy

    def project(self, location):
        ''' Project from world location to world position '''
        x = (location.x - location.y) * (self.tile_width / 2)
        y = (location.x + location.y - location.z) * (self.tile_height / 2)
        (w, h) = self.screen.get_size()
        projected = Vector2D(x + w / 2, y + h / 2);
        center = self.project_center()
        return projected - center

    def project_center(self):
        center_x = round(self.center.x, 1)
        center_y = round(self.center.y, 1)
        center_z = round(self.center.z, 1)
        x = (center_x - center_y) * (self.tile_width / 2)
        y = (center_x + center_y - center_z) * (self.tile_height / 2)
        return Vector2D(x, y)

    def pick_sprites(self, mouse_x, mouse_y):
        results = []

        for sprite in self.visible:
            is_picked = sprite.is_picked(self, mouse_x, mouse_y)
            if is_picked:
                results.append(sprite)
                parent = sprite.parent
                while parent is not None:
                    results.append(parent)
                    parent = parent.parent

        results.reverse()
        return results

    def get_tile_width(self):
        return self.tile_width

    def get_tile_height(self):
        return self.tile_height
