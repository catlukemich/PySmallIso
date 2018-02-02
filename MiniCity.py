from Tkinter  	import *
from Input    	import *
from Scene    	import *
from Viewport 	import *
from Scroller 	import *
from Sprite   	import *
from Terrain  	import *
from Heightmap 	import *
from utils    	import *

import pygame
import globals


class MiniCity():
	def __init__(self):
	
		pygame.init()
		pygame.display.set_caption("MiniCity")
		
		globals.screen = pygame.display.set_mode((800, 600))
		globals.input = Input()
		
		globals.viewport = Viewport()
		globals.scroller = Scroller()
		globals.scroller.enable()
		
		globals.land  = Scene()
		globals.world = Scene()
		
		img = loadImage("windmill.png")
		spr = Sprite(img)
		globals.land.addSprite(spr)
		
		hm = SimplexHeightmap(50,50)
		terrain = Terrain(hm)
		terrain.create()
		
		done  = False
		clock = pygame.time.Clock()
		while not done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
				else: 
					globals.input.handleEvent(event)
				
			
			self.redraw()
			
			pygame.display.flip()
		
			clock.tick(60)
		
		
	def redraw(self):
		globals.screen.fill((255,255,255))
		globals.viewport.draw()
		
		

game = MiniCity()


