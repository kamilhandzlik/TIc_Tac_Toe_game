import pygame as pg
import time

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
        # Placeholder, you need to assign proper images
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = (self.x, self.y)

    def clicked(self, x_value, y_value):
        global turn, won

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
                    check_winner("x")

                    if not won:
                        comp_move()

                else:
                    self.image = o_image
                    self.image = pg.transform.scale(
                        self.image, (self.width, self.height)
                    )
                    turn = "x"
                    check_winner("o")


def check_winner(player):
    global background, won

    for i in range(8):
        if (
            board[winning_list[i][0]] == player
            and board[winning_list[i][1]] == player
            and board[winning_list[i][2]] == player
        ):
            won = True
            break

    if won:
        Update()
        square_group.empty()
        background = pg.image.load(player.upper() + "Wins.png")
        background = pg.transform.scale(background, (WIDTH, HEIGHT))


def winner(player):
    global compmove, move

    for i in range(8):
        if (
            board[winning_list[i][0]] == player
            and board[winning_list[i][1]] == player
            and board[winning_list[i][2]] == ""
        ):
            compmove = winning_list[i][2]
            move = False
            break

        elif (
            board[winning_list[i][0]] == player
            and board[winning_list[i][1]] == ""
            and board[winning_list[i][2]] == player
        ):
            compmove = winning_list[i][1]
            move = False

        elif (
            board[winning_list[i][0]] == ""
            and board[winning_list[i][1]] == player
            and board[winning_list[i][2]] == player
        ):
            compmove = winning_list[i][0]
            move = False


def comp_move():
    global move, background
    move = True

    if move:
        winner("o")

    if move:
        winner("x")

    if move:
        check_danger_pos()

    if move:
        check_center()

    if move:
        check_corner()

    if move:
        check_edge()

    if not move:
        for square in squares:
            if square.number == compmove:
                square.clicked(square.x, square.y)

    else:
        Update()
        time.sleep(0.5)
        square_group.empty()
        background = pg.image.load("Tie Game.png")
        background = pg.transform.scale(background, (WIDTH, HEIGHT))


def check_danger_pos():
    global move, compmove

    if board == dangerpos1:
        compmove = 2
        move = False

    elif board == dangerpos2:
        compmove = 4
        move = False

    elif board == dangerpos3:
        compmove = 1
        move = False

    elif board == dangerpos4:
        compmove = 4
        move = False

    elif board == dangerpos5:
        compmove = 7
        move = False

    elif board == dangerpos6:
        compmove = 9
        move = False

    elif board == dangerpos7:
        compmove = 9
        move = False

    elif board == dangerpos8:
        compmove = 7
        move = False

    elif board == dangerpos9:
        compmove = 9
        move = False


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
x_wins_image = pg.image.load("XWins.png")
o_wins_image = pg.image.load("OWins.png")
BG_image = pg.image.load("background.png")
tie_image = pg.image.load("tie game.png")
background = pg.transform.scale(BG_image, (WIDTH, HEIGHT))


# main
move = True
won = False
compmove = 5

square_group = pg.sprite.Group()
squares = []
turn = "x"
winning_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7],
]

board = ["" for i in range(10)]

dangerpos1 = ["", "x", "", "", "", "o", "", "", "", "x"]
dangerpos2 = ["", "", "", "x", "", "o", "", "x", "", ""]
dangerpos3 = ["", "", "", "x", "x", "o", "", "", "", ""]
dangerpos4 = ["", "x", "", "", "", "o", "x", "", "", ""]
dangerpos5 = ["", "", "", "", "x", "o", "", "", "", "x"]
dangerpos6 = ["", "", "", "", "", "o", "x", "x", "", ""]
dangerpos7 = ["", "", "", "", "", "o", "x", "", "x", ""]
dangerpos8 = ["", "x", "", "", "", "o", "", "", "x", ""]
dangerpos9 = ["", "", "", "x", "", "o", "", "", "x", ""]

run = True
clock = pg.time.Clock()
num = 1


for y in range(1, 4):
    for x in range(1, 4):
        sq = Square(x, y, num)
        square_group.add(sq)
        squares.append(sq)
        num += 1


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
