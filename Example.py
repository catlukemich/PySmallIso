import iso
from Terrain import *
from Heightmap import *
import pygame


class Example():

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("PySmallIsoExample")
        icon = pygame.image.load("assets/icon.png")
        pygame.display.set_icon(icon)

        screen = pygame.display.set_mode((1800, 1000), pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE)
        self.screen = screen

        input = iso.Input()

        scene = iso.Scene()

        viewport = iso.Viewport(screen, scene)
        self.viewport = viewport

        scroller = iso.Scroller(viewport, input)
        scroller.enable()

        updater = iso.Updater()
        self.updater = updater

        sprite_picker = iso.SpritePicker(input, viewport)
        sprite_picker.enable()

        sprite_grabber = iso.SpriteGrabber(input, viewport)
        sprite_grabber.enable()

        img = iso.load_image("assets/truck.png")
        spr = ImageSprite(img)
        spr.layer = 1
        scene.add_sprite(spr)

        img = iso.load_image("assets/aircraft.png")
        spr = ImageSprite(img)
        spr.layer = 1
        spr.set_location(Vector3D(0.5, 0, 0))
        scene.add_sprite(spr)

        img = iso.load_image("assets/forklift.png")
        spr = ImageSprite(img)
        spr.layer = 1
        spr.set_location(Vector3D(0.5, 0.5, 0))
        scene.add_sprite(spr)

        hm = SimplexHeightmap(10, 10)
        terrain = Terrain(hm)
        scene.add_sprite(terrain)

        done = False
        clock = pygame.time.Clock()
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                else:
                    input.handle_event(event)

            self.redraw()
            self.update()
            pygame.display.flip()
            clock.tick(60)

    def redraw(self):
        self.screen.fill((255, 255, 255))
        self.viewport.draw()

    def update(self):
        self.updater.update()


if __name__ == "__main__":
    game = Example()
