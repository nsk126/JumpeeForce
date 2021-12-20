import pygame as pg
import sys
from settings import *
from tile import Tile
from level import Level

# setup
pg.init()
screen = pg.display.set_mode((screenWidth,screenHeight))
clock = pg.time.Clock()

#sprites
level = Level(lvl_MAP, screen)

# MAIN GAME LOOP
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        
    screen.fill('black')
    level.run()
    pg.display.update()
    clock.tick(60)