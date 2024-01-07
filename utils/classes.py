from .__init__ import *
from .settings import *

class SquareClass(pg.sprite.Sprite):
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





