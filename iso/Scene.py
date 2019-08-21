class SceneLayer:
  def __init__(self, name, index):
    self.name  = name
    self.index = index

    self.sprites = []



class Scene:
  def __init__(self):
    self.sprites = []
    self.layers = []
    
  def addLayer(self, layer_name, index):
    new_layer = SceneLayer(layer_name, index)
    self.layers.append(new_layer)
    self.layers.sort(cmp = self.sortLayers)

  def removeLayer(self, layer_name):
    for layer in self.layers:
      if layer.name == layer_name:
        self.layers.remove(layer)
    

  def sortLayers(self, layer1, layer2):
    return layer1.index - layer2.index


  def addSprite(self, layer_name, sprite):

    target_layer = None
    for layer in self.layers:
      if layer.name == layer_name:
        target_layer = layer

    target_layer.sprites.append(sprite)
  
  def removeSprite(self, layer_name, sprite):
    target_layer = None
    for layer in self.layers:
      if layer.name == layer_name:
        target_layer = layer

    target_layer.sprites.remove(sprite)
