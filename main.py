import pygame as pg
pg.init()
pg.font.init()

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


WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Tic Tac Toe game")

class SquareClass(pg.sprite.Sprite):          #zmieniłem nazwę klasy ponieważ VScode nie umiał rozróżnić między nią a modulo numpy
    def __init__(self, x_id, y_id, number):
        super().__init__()
        self.width = 120
        self.height = 120
        self.x = x_id * self.width          
        self.y = y_id * self.height
        self.content = ' '                                                      #atrybut pokazujący co ma być w kwadratach tworzących grę późiej będą do niego przypisywane obrazy
        self.number = number
        self.image = blank_image
        self.image = pg.transform.scale(self.image, (self.width, self.height))     #ta część działa przez podanie atrybutu do przeskalowania a następnie wartości po osiach do jakiego rozmiaru przez to treba było podać width i height
        self.rect = self.image.get_rect()                                       #prostokąt za pomocą, którego przesuwam cały obraz

    def update(self):                               #funkcja przesuwająca prostokąt do odpowiedniej lokalizacji
        self.rect.center =(self.x, self.y)           

#######################################
#### Importing images #################
#######################################
        

blank_image = pg.image.load('Blank.png')
x_image = pg.image.load('x.png')
o_image = pg.display.load('o.png')
x_wins_image = pg.display.load('X Wins.png')
o_wins_image = pg.display.load('O Wins.png')
BG_image = pg.display.load('Background.png')
tie_image = pg.display.load('Tie Game.png')

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



def Update():
    WIN.blit(background, (0, 0))  # Adjusted the arguments for blit
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

pg.quit()