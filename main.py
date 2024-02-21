import pygame as pg

pg.init()


# classes
class Square(pg.sprite.Sprite):
    def __init__(self, x_id, y_id, number):
        super().__init__()
        self.width = 120
        self.height = 120
        self.x = x_id * self.width
        self.y = y_id * self.height
        self.content = ""
        self.number = number
        self.image = blank_image
        self.image = pg.transform.scale(
            self.image, (self.width, self.height)
        )  # Placeholder, you need to assign proper images
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = (self.x, self.y)

    def clicked(self, x_value, y_value):
        global turn
        if self.content == "":
            if self.rect.collidepoint(x_value, y_value):
                self.content = turn
                board[self.number] = turn

                if turn == "x":
                    self.image = x_image
                    self.image = pg.transform.scale(
                        self.image, (self.width, self.height)
                    )
                    turn = "o"
                    comp_move()

                else:
                    self.image = o_image
                    self.image = pg.transform.scale(
                        self.image, (self.width, self.height)
                    )
                    turn = "x"


def comp_move():
    global move
    move = True

    if move:
        check_center()

    if move:
        check_corner

    if move:
        check_edge()

    if not move:
        for square in squares:
            if square.number == comp_move:
                square.clicked(square.x, square.y)


def check_center():
    global compmove, move

    if board[5] == "":
        compmove = 5
        move = False


def check_corner():
    global compmove, move

    for i in range(1, 11, 2):
        if i != 5:
            if board[i] == "":
                compmove = i
                move = False
                break


def check_edge():
    global compmove, move

    for i in range(2, 10, 2):
        if board[i] == "":
            compmove = i
            move = False
            break


def Update():
    WIN.blit(background, (0, 0))
    square_group.draw(WIN)
    square_group.update()
    pg.display.update()


# settings
FPS = 60

WIDTH, HEIGHT = 600, 600

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Tic Tac Toe game")


blank_image = pg.image.load("Blank.png")
x_image = pg.image.load("x.png")
o_image = pg.image.load("o.png")
x_wins_image = pg.image.load("X Wins.png")
o_wins_image = pg.image.load("O Wins.png")
BG_image = pg.image.load("Background.png")
tie_image = pg.image.load("Tie Game.png")
background = pg.transform.scale(BG_image, (WIDTH, HEIGHT))

move = True
compmove = 5


def get_font():
    return pg.font.SysFont("Calibri", 20)


# main

square_group = pg.sprite.Group()
squares = []
turn = "x"
board = ["" for i in range(10)]

num = 1
for y in range(1, 4):
    for x in range(1, 4):
        sq = Square(x, y, num)
        square_group.add(sq)
        squares.append(sq)
        num += 1


run = True
clock = pg.time.Clock()

while run:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN and turn == "x":
            mx, my = pg.mouse.get_pos()
            for s in squares:
                s.clicked(mx, my)

    Update()

pg.quit()
