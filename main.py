from utils import *
from utils.settings import *

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("TIc Tac Toe game")


run = True
clock = pg.time.Clock()

while run:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

pg.quit()