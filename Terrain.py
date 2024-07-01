from iso.SpriteComposite import SpriteComposite
from iso.utils import *
from iso.ImageSprite import *
from iso.SpriteComposite import SpriteComposite


class Terrain(SpriteComposite):
    def __init__(self, hm):
        super().__init__()
        self.hm = hm
        self.tiles = []
        self.create()

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

                img = load_image("assets/terrain/water_%d%d%d%d.png" % (h, h_r, h_b, h_br))

                if h == 0 or h_r == 0 or h_b == 0 or h_br == 0:
                    tile_type = Tile.WATER
                else:
                    tile_type = Tile.LAND

                tile = Tile(x, y, img, tile_type)
                tile.set_location(Vector3D(x, y, 0))

                self.add_sprite(tile)


class Tile(ImageSprite):
    WATER = 0
    LAND = 1

    def __init__(self, x, y, img, type):
        ImageSprite.__init__(self, img)
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
