from utils.classes import *   # Z jakiegoś powodu from utils import * nie chce mi zadziałać dlatego używam kilku importów bezpośrednio do porządanych plików
from utils.settings import *
from utils.__init__ import *

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("TIc Tac Toe game")



def Update():
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