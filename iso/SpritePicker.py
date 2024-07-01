from .Input import *


class SpritePicker(MouseListener):
    def __init__(self, input, viewport):
        self.viewport = viewport
        self.input = input

    def enable(self):
        self.input.add_mouse_listener(self)

    def mouseButtonDown(self, event):
        mouse_x = event.pos[0]
        mouse_y = event.pos[1]

        sprites = self.viewport.pick_sprites(mouse_x, mouse_y)
        if len(sprites) > 0:
            self.sprite_grabbed = sprites[0]
