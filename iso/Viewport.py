from functools import cmp_to_key

from .Rectangle import Rectangle
from .Vector2D import *
from .Vector3D import *
import threading
import time

# The tile width and height in pixels.
# Modify this values if you want tiles to be in different size.

class ViewportLayer:
    def __init__(self, scene_layer):
        self.scene_layer = scene_layer
        self.sprites = []

class Viewport:
    def __init__(self, screen, scene):
        self.screen = screen
        self.scene = scene
        self.tile_width = 128
        self.tile_height = 64

        self.center = Vector3D(0, 0)
        self.land_sprites = []
        self.world_sprites = []
        self.layers = []  # List of viewport layers



    def draw(self):
        viewport_layers = self.layers

        self.cull()
        for viewport_layer in viewport_layers:
            viewport_layer.sprites.sort(key=cmp_to_key(self.sortSprites))


        for layer in self.layers:
            for sprite in layer.sprites:
                sprite.draw(self, self.screen)

            # Debug code, uncomment to see the iso boundaries of each culling cell:
            # cells = layer.scene_layer.grid.cells
            # for cell_hash in cells:
            #     cell = cells[cell_hash]
            #     cell.drawIsoBoundaries(self, self.screen)


    # Sort the layers:
    def sortSprites(self, sprite1, sprite2):
        loc1 = sprite1.getLocation()
        loc2 = sprite2.getLocation()
        sum1 = loc1.x + loc1.y + loc1.z
        sum2 = loc2.x + loc2.y + loc2.z
        if sum1 > sum2:
            return 1
        else:
            return -1

    def cull(self):

        offset = 0  # The offset for culling sprites

        (w, h) = self.screen.get_size()

        viewport_layers = []

        # Cull the layers:
        for scene_layer in self.scene.layers:
            viewport_layer = ViewportLayer(scene_layer)
            viewport_layers.append(viewport_layer)
            # print "appending layer" + scene_layer.name

        for viewport_layer in viewport_layers:
            cells = viewport_layer.scene_layer.grid.cells
            for cell_hash in cells:
                cell = cells[cell_hash]
                if self.checkCellIntersects(cell):
                    for sprite in cell.sprites:
                        loc = sprite.getLocation()
                        pos = self.project(loc)
                        if pos.x > -offset and pos.x < w + offset and pos.y > -offset and pos.y < h + offset:
                            viewport_layer.sprites.append(sprite)

        self.layers = viewport_layers

    def checkCellIntersects(self, cell):
        (w, h) = self.screen.get_size()
        # Give the viewport rectangle a little offset so that cells nearby the
        # edges of the screen will also be checked when culling sprites:
        offset = 128
        viewport_rectangle = Rectangle(0 - offset, 0 - offset, w + 2*offset, h + 2* offset)
        cell_rectangle     = cell.getBoundaries(self)
        return viewport_rectangle.intersects(cell_rectangle)


    def getCenter(self):
        return Vector3D(self.center.x, self.center.y, 0)

    def setCenter(self, center):
        self.center = center

    def project(self, location):
        ''' Project from world location to world position '''
        x = (location.x - location.y) * (self.tile_width / 2)
        y = (location.x + location.y - location.z) * (self.tile_height / 2)
        (w, h) = self.screen.get_size()
        projected = Vector2D(x + w / 2, y + h / 2);
        center = self.projectCenter()
        return projected - center

    def projectCenter(self):
        x = (self.center.x - self.center.y) * (self.tile_width / 2)
        y = (self.center.x + self.center.y - self.center.z) * (self.tile_height / 2)
        return Vector2D(x, y)

    def pickSprites(self, mouse_x, mouse_y):

        picked_sprites = []

        for layer in self.layers:
            for sprite in layer.sprites:
                is_picked = sprite.isPicked(self, mouse_x, mouse_y)
                if is_picked:
                    picked_sprites.append(sprite)

        picked_sprites.reverse()
        return picked_sprites


    def getTileWidth(self):
        return self.tile_width

    def getTileHeight(self):
        return self.tile_height