import pygame
from tile import Tile
from settings import tile_size

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_lvl(level_data)

    def setup_lvl(self, layout):
        self.Tile = pygame.sprite.Group()
        for row_index,row in enumerate(layout):
            for col_index,col in enumerate(row):
                if col == 'X':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x,y),tile_size)
                    self.Tile.add(tile)
                #print(f'{row_index},{col_index}')
            
    def run(self):
        self.Tile.update(-1)
        self.Tile.draw(self.display_surface)