
class Vector2D:
	def __init__(self, x = 0, y =0):
		self.x = x
		self.y = y

		
	def sub(self, other):
		return Vector2D(self.x - other.x, self.y - other.y)