from functools import cmp_to_key

from .CullingGrid import CullingGrid


class Scene:
    def __init__(self, cell_size=20):
        self.cell_size = cell_size
        self.sprites = []
        self.layers = []

    def addLayer(self, layer_name, index):
        new_layer = SceneLayer(layer_name, index, self.cell_size)
        self.layers.append(new_layer)
        self.layers.sort(key=cmp_to_key(self.sortLayers))

    def removeLayer(self, layer_name):
        for layer in self.layers:
            if layer.name == layer_name:
                self.layers.remove(layer)

    def sortLayers(self, layer1, layer2):
        return layer1.index - layer2.index

    def addSprite(self, layer_name, sprite):
        target_layer = None
        for layer in self.layers:
            if layer.name == layer_name:
                target_layer = layer

        target_layer.addSprite(sprite)
        sprite.layer = target_layer

    def removeSprite(self, layer_name, sprite):
        target_layer = None
        for layer in self.layers:
            if layer.name == layer_name:
                target_layer = layer

        target_layer.removeSprite(sprite)
        sprite.layer = None

    def getCellSize(self):
        return self.cell_size


class SceneLayer:
    def __init__(self, name, index, cell_size):
        self.name = name
        print(index)
        self.index = index
        self.grid = CullingGrid(cell_size)

    def addSprite(self, sprite):
        self.grid.addSprite(sprite)

    def removeSprite(self, sprite):
        self.grid.removeSprite(sprite)

    def setSpriteLocation(self, sprite, old_location, new_location):
        self.grid.setSpriteLocation(sprite, old_location, new_location)
