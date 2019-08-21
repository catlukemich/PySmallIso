import random

import pygame
from pygame.locals import *

# Image loader functions
images = {}
def loadImage(path):
  global images
  if path in images:
    return images[path]
  else:
    img =  pygame.image.load(path).convert()
    img.set_colorkey((255,0,255), RLEACCEL)
    images[path]= img
    return img
