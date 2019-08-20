from Vector2D import *
from Vector3D import *
import threading
import time


class ViewportLayer:
  def __init__(self, scene_layer):
    self.scene_layer = scene_layer
    self.sprites = []

class Viewport:
  def __init__(self, screen, scene):
    self.screen = screen
    self.scene = scene
    self.center = Vector3D(0,0)
    self.land_sprites  = []
    self.world_sprites = []
    self.layers = []

    self.culled_and_sorted = False
    self.cull_and_sort_thread = threading.Thread(target = self.cull_and_sort)
    self.cull_and_sort_thread.daemon = True
    self.cull_and_sort_thread.start()
  

    
  def draw(self):
    for layer in self.layers:
      for sprite in layer.sprites:
        sprite.draw(self, self.screen)


  def cull_and_sort(self):
    
    offset = 256 # The offset for culling sprites

    while True:
      (w,h) = self.screen.get_size()   
      viewport_layers = []

      
      # Cull the layers: 
      for scene_layer in self.scene.layers:
        viewport_layer = ViewportLayer(scene_layer)
        viewport_layers.append(viewport_layer)
        #print "appending layer" + scene_layer.name

      for viewport_layer in viewport_layers:
        for sprite in viewport_layer.scene_layer.sprites:
          loc = sprite.getLocation()
          pos = self.project(loc)
          if pos.x > -offset and pos.x < w + offset and pos.y > -offset and pos.y < h + offset:
            viewport_layer.sprites.append(sprite)
    

      # Sort the layers:
      def sortSprites(sprite1, sprite2):
        loc1 = sprite1.getLocation()
        loc2 = sprite2.getLocation()
        return int(loc1.x + loc1.y + loc1.z) - int(loc2.x + loc2.y + loc2.z)

      for viewport_layer in viewport_layers:
        viewport_layer.sprites.sort(cmp=sortSprites)
        
      self.layers = viewport_layers


  def getCenter(self):
    return Vector3D(self.center.x, self.center.y, 0)
  
  def setCenter(self, center):
    self.center = center
    
  def project(self, location):
    ''' Project from world location to world position '''
    x = (location.x - location.y) * 64
    y = (location.x + location.y - location.z) * 32
    (w,h) = self.screen.get_size() 
    projected = Vector2D(x + w/2, y + h/2);
    center    = self.projectCenter()
    return projected - center
    
  def projectCenter(self):
    x = (self.center.x - self.center.y) * 64
    y = (self.center.x + self.center.y - self.center.z) * 32
    return Vector2D(x,y)
    
    
  def pickSprite(self, mouse_x, mouse_y):
    
    picked_sprites = []

    for layer in self.layers:
      for sprite in layer.sprites:
        is_picked = sprite.isPicked(self, mouse_x, mouse_y)
        if is_picked:
          picked_sprites.append(sprite)

    return picked_sprites

