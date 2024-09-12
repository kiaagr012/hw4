import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400

def draw():
    WIDTH = 400
    HEIGHT = 400
    r = 255
    g=0
    b = randint(120,255)

    for i in range(20):
        squ = Rect((0,0),(WIDTH,HEIGHT))
        squ.center = 150,150
        screen.draw.rect(squ,(r,g,b))
        r-=10
        g+=10
        WIDTH-=10
        HEIGHT+=10

pgzrun.go()