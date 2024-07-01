from .CullingStrategy import GridCullingStrategy
from .SortingStrategy import NearnessSortingStrategy

class Settings:
    def __init__(self, tile_width = 128, tile_height = 64, culling_strategy = GridCullingStrategy(), sorting_strategy = NearnessSortingStrategy()) -> None:
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.culling_strategy = culling_strategy
        self.sorting_strategy = sorting_strategy

class Defaults:

    instance = Settings()  # The Defaults instance used across the isometric engine package. Can be changed through Defaults.set(defaults)  static method.


    @staticmethod
    def set(settings: Settings):
        Defaults.instance = settings

    @staticmethod
    def get():
        return Defaults.instance

if __name__ == "__main__":
    defaults = Defaults(128, 256)

    Defaults.set(defaults)

    print(vars(defaults))
    print(vars(Defaults.instance))