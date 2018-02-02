from Input    import *
from Vector2D import *

import globals

class Scroller(MouseListener):
	def __init__(self):
		self.rmb_down  = False
		pass
		
		
	def enable(self):
		globals.input.addMouseListener(self)
		
	def mouseButtonDown(self, event):
		print(event)
		if event.button == 3:
			self.rmb_down = True
				
	def mouseMotion(self, event):
		if self.rmb_down:
			c = globals.viewport.getCenter()
			if event.rel[0] is not 0:
				c.x += 0.1 * event.rel[0]
				c.y -= 0.1 * event.rel[0]
			if event.rel[1] is not 0:
				pass
				c.x += 0.1 * event.rel[1]
				c.y += 0.1 * event.rel[1]
				
			
			globals.viewport.setCenter(c)
		
	def mouseButtonUp(self, event):
		if event.button == 3:
			self.rmb_down = False
		
	def disable(self):
		globals.input.removeMouseListener(self)