from Vector3D import *
import globals


class Sprite:
	def __init__(self, image = None):
		self.image = image
		self.location = Vector3D()
		pass
	
	
	def draw(self):
		position = globals.viewport.project(self.location)
		(w, h) = self.image.get_size()
		globals.screen.blit(self.image, (position.x - w/2, position.y - h/2))

		
	def setLocation(self, loc):
		self.location = loc
		
	def getLocation(self):
		return self.location