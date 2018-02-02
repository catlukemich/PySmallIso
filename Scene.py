
class Scene:
	def __init__(self):
		self.sprites = []
		
	def addSprite(self, sprite):
		self.sprites.append(sprite)
	
	def removeSprite(self, sprite):
		self.sprites.remove(sprite)
