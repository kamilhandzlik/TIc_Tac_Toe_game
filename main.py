from utils.classes import *
from utils.settings import *

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Tic Tac Toe game")



def Update():
    WIN.blit(background, WIDTH, HEIGHT)
    pg.display.update()


run = True
clock = pg.time.Clock()

while run:
    clock.tick(FPS)
    SquareClass()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    Update()
    

pg.quit()