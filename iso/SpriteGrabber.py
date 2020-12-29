from .Input import *
from .Viewport import *


class SpriteGrabber(MouseListener):
    def __init__(self, input, viewport):
        self.input = input
        self.viewport = viewport
        self.sprite_grabbed = None

    def enable(self):
        self.input.addMouseListener(self)

    def mouseButtonDown(self, event):
        if event.button == 1:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            sprites = self.viewport.pickSprites(mouse_x, mouse_y)
            if len(sprites) > 0:
                self.sprite_grabbed = sprites[0]

    def mouseMotion(self, event):
        tile_width = self.viewport.tile_width
        tile_height = self.viewport.tile_height

        dx = event.rel[0]
        dy = event.rel[1]

        if self.sprite_grabbed != None:
            old_loc = self.sprite_grabbed.getLocation()
            loc = Vector3D(old_loc.x, old_loc.y, old_loc.z)
            loc.x += float(dx) / tile_width
            loc.y -= float(dx) / tile_width

            loc.x += float(dy) / tile_height
            loc.y += float(dy) / tile_height
            self.sprite_grabbed.setLocation(loc)

    def disable(self):
        self.input.removeMouseListener(self)

    def mouseButtonUp(self, event):
        if event.button == 1:
            self.sprite_grabbed = None
