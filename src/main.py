import pygame
import sys

from settings import _screenWidht, _screenHeight, level_map
from tiles import Tile
from level import Level

# pygame setup function
pygame.init()

#screenbox
_screenReso = (_screenWidht,_screenHeight)

#create screen and init clock
screen = pygame.display.set_mode(_screenReso)
clk = pygame.time.Clock()

#create level
level = Level(level_map, screen)

#game loop
while True:
    
    #event checker
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #filling screen black
    screen.fill('black')

    #run level
    level.run()

    #set pygame nxt update frame and clock tick rate
    pygame.display.update()
    clk.tick(60)