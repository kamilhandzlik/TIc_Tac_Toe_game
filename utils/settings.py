import pygame as pg
from utils import *
from utils.classes import SquareClass
pg.init()


WHITE = (255, 255, 255)         #lines
BLACK = (0, 0, 0)               #text
RED = (255, 0, 0)               # X
BLUE = (0, 0, 255)              #background color
GREEN = (0, 255, 0)             # O


FPS = 60

WIDTH, HEIGHT = 600, 600

ROWS = COLS = 100

PIXEL_SIZE = PIXEL_SIZE = WIDTH // COLS

BG_COLOR = BLUE

def grt_font():
    return pg.font.SysFont("Calibri", 20)

#######################################
#### Importing images #################
#######################################
blank_image = pg.image.load('utils/Blank.png')
x_image = pg.image.load('utils/x.png')
o_image = pg.display.load('utils/o.png')
x_wins_image = pg.display.load('utils/X Wins.png')
o_wins_image = pg.display.load('utils/O Wins.png')
BG_image = pg.display.load('utils/Background.png')
tie_image = pg.display.load('utils/Tie Game.png')

background = pg.transform.scale(BG_image, (WIDTH, HEIGHT))      #Tutaj skaluję obraz z tyłu do wielkości wyświetlacza mojej gry
square_group = pg.sprite.Group()
squares = []
 
num = 1
for y in range(1, 4):
    for x in range(1, 4):
        sq = SquareClass(x, y, num)
        square_group.add(sq)
        squares.append(sq)

        num += 1

