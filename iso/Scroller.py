from .Input    import *
from .Vector2D import *



class Scroller(MouseListener):
  def __init__(self, viewport, input):
    self.rmb_down  = False
    self.viewport = viewport
    self.input = input
    pass
    
    
  def enable(self):
    self.input.addMouseListener(self)
    
  def mouseButtonDown(self, event):
    if event.button == 3:
      self.rmb_down = True
        
  def mouseMotion(self, event):
    if self.rmb_down:
      c = self.viewport.getCenter()
      if event.rel[0] is not 0:
        c.x += 0.1 * event.rel[0]
        c.y -= 0.1 * event.rel[0]
      if event.rel[1] is not 0:
        pass
        c.x += 0.1 * event.rel[1]
        c.y += 0.1 * event.rel[1]
        
      
      self.viewport.setCenter(c)
    
  def mouseButtonUp(self, event):
    if event.button == 3:
      self.rmb_down = False
    
  def disable(self):
    self.input.removeMouseListener(self)