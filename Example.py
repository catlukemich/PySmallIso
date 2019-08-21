from Tkinter        import *
from Input          import *
from Scene          import *
from Viewport       import *
from Scroller       import *
from SpritePicker   import *
from SpriteGrabber  import *
from Sprite         import *
from Updateables    import *
from Terrain        import *
from Heightmap      import *
from utils          import *
from Vector3D       import *


import pygame


class Example():
  def __init__(self):
  
    pygame.init()
    pygame.display.set_caption("PySmallIsoExample")
    
    
    screen = pygame.display.set_mode((1024, 768), pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE )
    self.screen = screen

    input = Input()
    
    scene  = Scene()
    scene.addLayer("Land", 0)
    scene.addLayer("Overlays", 1)
    scene.addLayer("Overground", 2)
    
    viewport = Viewport(screen, scene)
    self.viewport = viewport

    scroller = Scroller(viewport, input)
    scroller.enable()

    updater = Updater()
    self.updater = updater

    sprite_picker = SpritePicker(input, viewport)
    sprite_picker.enable()

    sprite_grabber = SpriteGrabber(input, viewport)
    sprite_grabber.enable()

    img = loadImage("assets/truck.png")
    spr = Sprite(img)
    scene.addSprite("Overground", spr)
    
    img = loadImage("assets/aircraft.png")
    spr = Sprite(img)
    spr.setLocation(Vector3D(0.5,0,0))
    scene.addSprite("Overground", spr)

    img = loadImage("assets/forklift.png")
    spr = Sprite(img)
    spr.setLocation(Vector3D(0.5,0.5,0))
    scene.addSprite("Overground", spr)
    
    hm = SimplexHeightmap(200,200)
    terrain = Terrain(hm)
    tiles = terrain.create()

    for tile in tiles:
      scene.addSprite("Land", tile)
   

    done  = False
    clock = pygame.time.Clock()
    while not done:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True
        else: 
          input.handleEvent(event)
        
      
      self.redraw()
      self.update()
      pygame.display.flip()
    
      clock.tick(60)
    
    
  def redraw(self):
    self.screen.fill((255,255,255))
    self.viewport.draw()
    
  def update(self):
    self.updater.update()
    
if __name__ == "__main__":
  game = Example()


