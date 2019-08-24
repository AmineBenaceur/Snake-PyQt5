#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from Constants import *
from Cube import *
from Snake import *
from pygame import *

class Window(QWindow):
    def __init__(self):
        QWindow.__init__(self)
        self.setTitle("Window")
        self.resize(WINDOW_HEIGHT,WINDOW_WIDTH )

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())

def drawGrid(w, rows, surface):
    pass
def reDrawWindow(surface):
    pass
def randomSnack(rows, items):
    pass
def message_box(subject,content):
    pass
def main():
    s = Snake(RED, (10,10))

    flag = True
    clock = pygame.time.clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)



    pass


