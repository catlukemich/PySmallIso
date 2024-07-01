import abc
from functools import cmp_to_key

class SortingStrategy(abc.ABC):
    ''' 
    The sorting strategy that depends on what is the functionality the user code wants to use when sorting isometric viewports.
    Instances of this abstract class can be set on individual viewport instnances using Viewport.set_sorting_strategy(strategy)
    instance method.
    '''

    @abc.abstractmethod
    def sort_sprites(self, sprites) -> None:
        ''' The method called by the Viewport to sort sprites the viewport has already culled '''
        pass


class DisabledSortingStrategy(SortingStrategy):
    '''
    A sorting strategy that actually doesn't do anything - doesn't perform any sorting.
    In other words- a "null object" design pattern implementation of SortingStrategy. 
    '''
    
    def sort_sprites(self, sprite1, sprite2) -> None:
        return 0


class OnlyLayersSortingStrategy(SortingStrategy):
    '''
    A sorting strategy that implements sorting only basing on the layers inidices assigned to isometric sprites.
    '''

    def sort_sprites(self, sprites : list) -> None:
        sprites.sort(key= cmp_to_key(self.compare_sprites))  # Sort the sprites using the own compare_sprites method as comparator function.


    def compare_sprites(self, sprite1, sprite2) -> int:
        layer1 = sprite1.layer
        layer2 = sprite2.layer
        return layer1 - layer2


class NearnessSortingStrategy(OnlyLayersSortingStrategy):
    ''' 
    The trivial (yet the fastest) sorting strategy basing on the notion of "nearness" of isometric sprites, which should be understood
    as a distance from such sprite to the origin of the view - the "eye" of the viewer of the isometric viewport.
    '''

    def compare_sprites(self, sprite1, sprite2) -> int:
        ''' Because this sorting strategy inherits from OnlyLayersSorting strategy, this comparator method only overrides the super implementation '''
        layers_diff = super().compare_sprites(sprite1, sprite2)
        if layers_diff != 0:
            return layers_diff

        loc1 = sprite1.get_location()
        loc2 = sprite2.get_location()
        nearness1 = loc1.x + loc1.y + loc1.z
        nearness2 = loc2.x + loc2.y + loc2.z

        # TODO: This might be wrong!
        if nearness1 > nearness2:
            return 1
        elif nearness2 < nearness1:
            return -1
        else:
            return 0

