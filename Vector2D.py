import math

class Vector2D:
  def __init__(self, x = 0, y =0):
    self.x = x
    self.y = y

    
  def __sub__(self, other):
    return Vector2D(self.x - other.x, self.y - other.y)

  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)

  def __mult__(self, factor):
    return Vector2D(self.x * factor, self.y * factor)

  def normalize(self):
    length = self.length()
    self.x = self.x / length
    self.y = self.y / length

  def length(self):
    return sqrt(self.x * self.x, self.y * self.y)

  def __gt__(self, other):
    return (self.x > other.x and self.y > other.y)

  def __lt__(self, other):
    return (self.x < other.x and self.y < other.y)

  def __str__(self):
    return "Vector2D: (" + str(self.x) + ", " + str(self.y) + ")"
  
