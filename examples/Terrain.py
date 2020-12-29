from iso.utils import *
from iso.Sprite import *


class Terrain:
    def __init__(self, hm):
        self.hm = hm
        self.tiles = []
        pass

    def create(self):
        for y in range(0, self.hm.height - 1):
            for x in range(0, self.hm.width - 1):
                index_h = y * self.hm.width + x
                index_r = y * self.hm.width + x + 1
                index_b = (y + 1) * self.hm.width + x
                index_br = (y + 1) * self.hm.width + x + 1

                h = self.hm.heights[index_h]
                h_r = self.hm.heights[index_r]
                h_b = self.hm.heights[index_b]
                h_br = self.hm.heights[index_br]

                img = loadImage("assets/terrain/water_%d%d%d%d.png" % (h, h_r, h_b, h_br))

                if h == 0 or h_r == 0 or h_b == 0 or h_br == 0:
                    tile_type = Tile.WATER
                else:
                    tile_type = Tile.LAND

                tile = Tile(x, y, img, tile_type)
                tile.setLocation(Vector3D(x, y, 0))

                self.tiles.append(tile)

        return self.tiles


class Tile(Sprite):
    WATER = 0
    LAND = 1

    def __init__(self, x, y, img, type):
        Sprite.__init__(self, img)
        self.x = x
        self.y = y
        self.type = type


if __name__ == "__main__":
    hm = SimplexHeightmap(20, 20)
    for y in range(0, hm.height):
        for x in range(0, hm.width):
            index = y * hm.width + x
            print("{0:3.0f}".format(hm.heights[index])),
        print("\n")
    raw_input()
