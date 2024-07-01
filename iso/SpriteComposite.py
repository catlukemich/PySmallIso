from .Sprite import Sprite


class SpriteComposite(Sprite):

    def __init__(self):
        super().__init__()
        self.children = []

    def set_scene(self, scene):
        for child in self.children:
            child_scene = child.get_scene()
            if child_scene is None and scene is not None:
                scene.add_sprite(child)
            elif child_scene is not None and scene is None:
                scene.remove_sprite(child)

            if child_scene is not None and scene is not None:
                if child_scene != scene:
                    child_scene.remove_sprite(child)
                    scene.add_sprite(child)

        super().set_scene(scene)

    def add_sprite(self, sprite):
        self.children.append(sprite)
        sprite.parent = self
        scene = self.get_scene()
        if scene is not None:
            scene.add_sprite(sprite)

    def remove_sprite(self, sprite):
        self.children.remove(sprite)
        sprite.parent = None
        scene = self.get_scene()
        if scene is not None:
            scene.remove_sprite(sprite)

    def set_location(self, location):
        old_location = self.get_location()
        new_location = location
        delta = new_location - old_location

        for child in self.children:
            old_child_location = child.get_location()
            new_child_location = old_child_location + delta
            child.set_location(new_child_location)

        super().set_location(location)


    def draw(self, viewport, surface):
        pass