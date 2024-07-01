from .Vector3D import Vector3D
from .Vector2D import Vector2D
from .Sprite import Sprite

class ImageSprite(Sprite):
    def __init__(self, image=None):
        super().__init__()
        self.image = image  # The image to render this sprite


    def draw(self, viewport, screen):
        location = self.get_location()
        position = viewport.project(location)
        (w, h) = self.image.get_size()
        screen.blit(self.image, (position.x - w / 2, position.y - h / 2))

    def is_picked(self, viewport, mouse_x, mouse_y):
        location = self.get_location()
        position = viewport.project(location)
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
