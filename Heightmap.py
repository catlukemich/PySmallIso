from Noise import *


class Heightmap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.heights = []
        for y in range(0, height):
            for x in range(0, width):
                self.heights.append(0)
        self.createHeights()
        self.normalizeHeights()

    def createHeights(self):
        pass

    def normalizeHeights(self):
        ''' Normalize heights so that the map could render tiles with deltas up to 1 '''
        for y in range(0, self.height):
            for x in range(0, self.width):
                index = y * self.width + x
                height = self.heights[index]
                if height > 5:
                    height = 1
                else:
                    height = 0
                self.heights[index] = height


class SimplexHeightmap(Heightmap):
    def createHeights(self):
        noise = SimplexNoise()
        for y in range(0, self.height):
            for x in range(0, self.width):
                index = y * self.width + x
                h = noise.noise2(x / 10.0, y / 10.0)
                h *= 100
                h += 10
                self.heights[index] = h
