import pygame as pg
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
    pg.font.SysFont("Calibri", 20)