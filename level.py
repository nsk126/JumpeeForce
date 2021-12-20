from sys import platform
import pygame
from tile import Tile
from settings import tile_size, screenWidth
from player import Player

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_lvl(level_data)
        self.world_shift = 0

    def setup_lvl(self, layout):
        self.Tile = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        
        for row_index,row in enumerate(layout):
            for col_index,col in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if col == 'X':
                    tile = Tile((x,y),tile_size)
                    self.Tile.add(tile)
                if col == 'P':
                     x = col_index * tile_size
                     y = row_index * tile_size
                     player_sprite = Player((x,y))
                     self.player.add(player_sprite)

                #print(f'{row_index},{col_index}')

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screenWidth / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screenWidth - (screenWidth / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8        

    def run(self):
        #level tiles
        self.Tile.update(self.world_shift)
        self.Tile.draw(self.display_surface)
        
        #player
        self.player.update()
        self.player.draw(self.display_surface)
        self.scroll_x()