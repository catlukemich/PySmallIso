from functools import cmp_to_key
from .Vector2D import *
from .Vector3D import *
import threading
import time

# The tile width and height in pixels.
# Modify this values if you want tiles to be in different size.
TILE_WIDTH  = 128
TILE_HEIGHT = 64

# Precalculated half tile dimensions, dont touch that
HALF_TILE_WIDTH = TILE_WIDTH / 2
HALF_TILE_HEIGHT = TILE_HEIGHT / 2


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
    self.layers = [] # List of viewport layers

    self.culled_and_sorted = False
    self.cull = threading.Thread(target = self.cull_and_sort)
    self.cull.daemon = True
    self.cull.start()
  

    
  def draw(self):
    viewport_layers = self.layers
    for viewport_layer in viewport_layers:
      viewport_layer.sprites.sort(key = cmp_to_key(self.sortSprites))

    for layer in self.layers:
      for sprite in layer.sprites:
        sprite.draw(self, self.screen)

  # Sort the layers:
  def sortSprites(self, sprite1, sprite2):
    loc1 = sprite1.getLocation()
    loc2 = sprite2.getLocation()
    sum1 = loc1.x + loc1.y + loc1.z
    sum2 = loc2.x + loc2.y + loc2.z
    if sum1 > sum2: return 1
    else: return -1

   

  def cull_and_sort(self):
    
    offset = 256 # The offset for culling sprites

    (w,h) = self.screen.get_size()   
    while True:
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
    
   
      self.layers = viewport_layers


  def getCenter(self):
    return Vector3D(self.center.x, self.center.y, 0)
  
  def setCenter(self, center):
    self.center = center
    
  def project(self, location):
    ''' Project from world location to world position '''
    x = (location.x - location.y) * HALF_TILE_WIDTH
    y = (location.x + location.y - location.z) * HALF_TILE_HEIGHT
    (w,h) = self.screen.get_size() 
    projected = Vector2D(x + w/2, y + h/2);
    center    = self.projectCenter()
    return projected - center
    
  def projectCenter(self):
    x = (self.center.x - self.center.y) * HALF_TILE_WIDTH
    y = (self.center.x + self.center.y - self.center.z) * HALF_TILE_HEIGHT
    return Vector2D(x,y)
    
    
  def pickSprites(self, mouse_x, mouse_y):
    
    picked_sprites = []

    for layer in self.layers:
      for sprite in layer.sprites:
        is_picked = sprite.isPicked(self, mouse_x, mouse_y)
        if is_picked:
          picked_sprites.append(sprite)
    
    picked_sprites.reverse()
    return picked_sprites

