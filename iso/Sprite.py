from .Vector3D import *
from .Vector2D import *


class Sprite:
    def __init__(self, image=None):
        self.layer = None
        self.image = image  # The image to render this sprite
        self.location = Vector3D()  # Location of the sprite in isometric 3d world coordinates

    def draw(self, viewport, screen):
        position = viewport.project(self.location)
        (w, h) = self.image.get_size()
        screen.blit(self.image, (position.x - w / 2, position.y - h / 2))

    def setLocation(self, loc, update_grid = True):
        if update_grid and self.layer != None:
          old_location = self.getLocation()
          new_location = loc

        self.location = loc

        if update_grid and self.layer != None:
          self.layer.setSpriteLocation(self, old_location, new_location)

    def getLocation(self):
        return Vector3D(self.location.x, self.location.y, self.location.z)

    def isPicked(self, viewport, mouse_x, mouse_y):
        position = viewport.project(self.location)
        (w, h) = self.image.get_size()

        top_left = Vector2D(position.x - w / 2, position.y - h / 2)
        bottom_right = Vector2D(position.x + w / 2, position.y + h / 2)
        mouse = Vector2D(mouse_x, mouse_y)

        if mouse > top_left and mouse < bottom_right:

            mouse_relative = mouse - top_left
            color = self.image.get_at((int(mouse_relative.x), int(mouse_relative.y)))
            if color.r == 255 and color.g == 0 and color.b == 255:
                return False
            else:
                return True
        else:
            return False
