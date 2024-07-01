from .Rectangle import Rectangle

class CullingStrategy:

    def cull(self, screen, scene, viewport):
        pass


class GridCullingStrategy(CullingStrategy):

    def cull(self, screen, scene, viewport):
        offset = 0  # The offset for culling sprites
        (w, h) = screen.get_size()

        grid = scene.get_grid()
        cells = grid.get_cells()
        visible = []

        for cell_hash in cells:
            cell = cells[cell_hash]
            if self.check_cell_intersects(screen, viewport, cell):
                for sprite in cell.sprites:
                    loc = sprite.get_location()
                    pos = viewport.project(loc)
                    if -offset < pos.x < w + offset and -offset < pos.y < h + offset:
                        visible.append(sprite)

        return visible

    def check_cell_intersects(self, screen, viewport, cell):
        (w, h) = screen.get_size()
        # Give the viewport rectangle a little offset so that cells nearby the
        # edges of the screen will also be checked when culling sprites:
        offset = 128
        viewport_rectangle = Rectangle(0 - offset, 0 - offset, w + 2 * offset, h + 2 * offset)
        cell_rectangle = cell.get_boundaries(viewport)
        return viewport_rectangle.intersects(cell_rectangle)


class NeverCullStrategy(CullingStrategy):

    def cull(self, screen, scene, viewport):
        grid = scene.get_grid()
        cells = grid.get_cells()
        visible = []
        for cell_hash in cells:
            cell = cells[cell_hash]
            for sprite in cell.sprites:
                visible.append(sprite)

        return visible