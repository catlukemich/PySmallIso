import pygame
from .Rectangle import Rectangle
from .Vector3D import Vector3D
from math import *

class CullingGrid:

    def __init__(self, cell_size):
        self.cells = {}
        self.cell_size = cell_size

    def getCellSize(self):
        return self.cell_size

    def setSpriteLocation(self, sprite, old_location, new_location):
        hash_old = self.calcCellHashByLocation(old_location)
        hash_new = self.calcCellHashByLocation(new_location)
        if hash_old != hash_new:
            print("Move")
            old_cell = self.cells[hash_old]
            old_cell.removeSprite(sprite)
            self.addSprite(sprite)

    def addSprite(self, sprite):
        hash = self.calcCellHash(sprite)
        cell = None
        if hash in self.cells:
            cell = self.cells[hash]
        else:
            sprite_location = sprite.getLocation()
            cell_location = self.calcCellLocation(sprite_location)
            cell = CullingCell(self, cell_location)
            self.cells[hash] = cell

        cell.addSprite(sprite)


    def removeSprite(self, sprite):
        hash = self.calcCellHash(sprite)
        if hash in self.cells:
            cell = self.cells[hash]
            cell.removeSprite(sprite)



    def calcCellHash(self, sprite):
        sprite_loc = sprite.getLocation()
        return self.calcCellHashByLocation(sprite_loc)

    def calcCellHashByLocation(self, location):
        cell_location = self.calcCellLocation(location)
        hash = str(cell_location.x) + "/" + str(cell_location.y)
        return hash

    def calcCellLocation(self, spatial_location):
        cell_x = floor(spatial_location.x / self.cell_size) * self.cell_size + self.cell_size / 2
        cell_y = floor(spatial_location.y / self.cell_size) * self.cell_size + self.cell_size / 2
        return Vector3D(cell_x, cell_y, 0)



class CullingCell:
    def __init__(self, grid, location):
        self.grid = grid
        self.location = location
        self.sprites = []


    def addSprite(self, sprite):
        self.sprites.append(sprite)


    def removeSprite(self, sprite):
        self.sprites.remove(sprite)

    def getBoundaries(self, viewport):
        cell_size = self.grid.getCellSize()
        cell_center = viewport.project(self.location)
        offset_horizontal = cell_size / 2 * viewport.getTileWidth()
        offset_vertical   = cell_size / 2 * viewport.getTileHeight()

        cell_left   = cell_center.x - offset_horizontal
        cell_top    = cell_center.y - offset_vertical

        cell_width  = 2 * offset_horizontal
        cell_height = 2 * offset_vertical

        return Rectangle(cell_left, cell_top, cell_width, cell_height)

    def drawIsoBoundaries(self, viewport, surface):

        cell_size = self.grid.getCellSize()
        cell_center = viewport.project(self.location)
        offset_horizontal = cell_size / 2 * viewport.getTileWidth()
        offset_vertical = cell_size / 2 * viewport.getTileHeight()

        cell_left = cell_center.x - offset_horizontal
        cell_top = cell_center.y - offset_vertical

        cell_width = 2 * offset_horizontal
        cell_height = 2 * offset_vertical

        pygame.draw.line(surface, (0, 0, 0), (cell_left, cell_center.y), (cell_center.x, cell_top), 2)
        pygame.draw.line(surface, (0, 0, 0), (cell_center.x, cell_top), (cell_left + cell_width, cell_center.y), 2)
        pygame.draw.line(surface, (0, 0, 0), (cell_left + cell_width, cell_center.y), (cell_center.x, cell_top + cell_height), 2)
        pygame.draw.line(surface, (0, 0, 0), (cell_center.x, cell_top + cell_height), (cell_left, cell_center.y), 2)

        font = pygame.font.SysFont("Arial", 16)
        pos_string = f"(Cell: {self.location.x}, {self.location.y}"
        text_surface = font.render(pos_string, True, (0,0,0))
        surface.blit(text_surface, (cell_center.x, cell_center.y))

