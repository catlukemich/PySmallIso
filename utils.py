import random

import pygame
from pygame.locals import *

# Image loader functions
def loadImage(path):
  img = pygame.image.load(path).convert()
  img.set_colorkey((0,0,0), RLEACCEL)
  return img
