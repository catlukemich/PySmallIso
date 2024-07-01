from typing import List

import pygame
from .Rectangle import Rectangle
from .Vector3D import Vector3D
from math import *


class CullingGrid:

    def __init__(self, cell_size):
        self.__cells = {}
        self.__cell_size = cell_size

    @property
    def cells(self):
        return self.__cells

    def get_cells(self):
        return self.__cells

    def get_cell_size(self):
        return self.__cell_size

    def update_sprite_location(self, sprite, old_location, new_location):
        hash_old = self.calc_cell_hash_by_location(old_location)
        hash_new = self.calc_cell_hash_by_location(new_location)

        if hash_old != hash_new:
            self.remove_sprite(sprite, old_location)
            self.add_sprite(sprite, new_location)

    def add_sprite(self, sprite, location):
        hash   = self.calc_cell_hash_by_location(location)
        if hash in self.__cells:
            cell = self.__cells[hash]
        else:
            sprite_location = sprite.get_location()
            cell_location = self.calc_cell_location(sprite_location)
            cell = CullingCell(self, cell_location)
            self.__cells[hash] = cell

        cell.add_sprite(sprite)

    def remove_sprite(self, sprite, location):
        hash = self.calc_cell_hash_by_location(location)
        if hash in self.__cells:
            cell = self.__cells[hash]
            cell.remove_sprite(sprite)

    def calc_cell_hash(self, sprite):
        sprite_loc = sprite.get_location()
        return self.calc_cell_hash_by_location(sprite_loc)

    def calc_cell_hash_by_location(self, location):
        cell_location = self.calc_cell_location(location)
        hash = str(cell_location.x) + "/" + str(cell_location.y)
        return hash

    def calc_cell_location(self, spatial_location):
        cell_x = floor(spatial_location.x / self.__cell_size) * self.__cell_size + self.__cell_size / 2
        cell_y = floor(spatial_location.y / self.__cell_size) * self.__cell_size + self.__cell_size / 2
        return Vector3D(cell_x, cell_y, 0)


class CullingCell:
    def __init__(self, grid, location):
        self.__grid = grid
        self.__location = location
        self.__sprites = []

    @property
    def location(self):
        return self.__location

    @property
    def sprites(self):
        return self.__sprites

    def add_sprite(self, sprite):
        if not sprite in self.__sprites:
            self.__sprites.append(sprite)

    def remove_sprite(self, sprite):
        if sprite in self.__sprites:
            self.__sprites.remove(sprite)

    def get_boundaries(self, viewport):
        cell_size = self.__grid.get_cell_size()
        cell_center = viewport.project(self.__location)
        offset_horizontal = cell_size / 2 * viewport.get_tile_width()
        offset_vertical = cell_size / 2 * viewport.get_tile_height()

        cell_left = cell_center.x - offset_horizontal
        cell_top = cell_center.y - offset_vertical

        cell_width = 2 * offset_horizontal
        cell_height = 2 * offset_vertical

        return Rectangle(cell_left, cell_top, cell_width, cell_height)

    def draw_iso_boundaries(self, viewport, surface):
        cell_size = self.__grid.get_cell_size()
        cell_center = viewport.project(self.__location)
        offset_horizontal = cell_size / 2 * viewport.get_tile_width()
        offset_vertical = cell_size / 2 * viewport.get_tile_height()

        cell_left = cell_center.x - offset_horizontal
        cell_top = cell_center.y - offset_vertical

        cell_width = 2 * offset_horizontal
        cell_height = 2 * offset_vertical

        pygame.draw.line(surface, (0, 0, 0), (cell_left, cell_center.y), (cell_center.x, cell_top), 2)
        pygame.draw.line(surface, (0, 0, 0), (cell_center.x, cell_top), (cell_left + cell_width, cell_center.y), 2)
        pygame.draw.line(surface, (0, 0, 0), (cell_left + cell_width, cell_center.y),
                         (cell_center.x, cell_top + cell_height), 2)
        pygame.draw.line(surface, (0, 0, 0), (cell_center.x, cell_top + cell_height), (cell_left, cell_center.y), 2)

        font = pygame.font.SysFont("Arial", 16)
        pos_string = f"(Cell: {self.__location.x}, {self.__location.y}"
        text_surface = font.render(pos_string, True, (0, 0, 0))
        surface.blit(text_surface, (cell_center.x, cell_center.y))

    def __str__(self):
        return "CullingCell: " + str(self.__location.x) + "/" + str(self.__location.y)