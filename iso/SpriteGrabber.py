from .Input import *
from .Viewport import *

class SpriteGrabber(MouseListener):
  def __init__(self, input, viewport):
    self.input = input
    self.viewport = viewport
    self.sprite_grabbed = None
    pass

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
    dx = event.rel[0]
    dy = event.rel[1]
    
    if self.sprite_grabbed != None:
      loc = self.sprite_grabbed.getLocation()
      loc.x += float(dx) / TILE_WIDTH
      loc.y -= float(dx) / TILE_WIDTH
      
      loc.x += float(dy) / TILE_HEIGHT
      loc.y += float(dy) / TILE_HEIGHT
      self.sprite_grabbed.setLocation(loc)

  def disable(self):
    self.input.removeMouseListener(self)

  def mouseButtonUp(self, event):
    if event.button == 1:
      self.sprite_grabbed = None