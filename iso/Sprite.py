from .Vector3D import Vector3D


class Sprite:

    def __init__(self):
        self.layer = 0
        self.location = Vector3D()  # Location of the sprite in isometric 3d world coordinates
        self.scene = None
        self.parent = None

    def draw(self, viewport):
        pass

    def get_location(self):
        return self.location

    def set_location(self, location):
        old_location = self.location
        new_location = location

        scene = self.get_scene()
        if scene is not None:
            scene.update_sprite_location(self, old_location, new_location)

        self.location = location

    def set_scene(self, scene):
        self.scene = scene

    def get_scene(self):
        return self.scene

    def is_picked(self, viewport, mouse_x, mouse_y):
        pass