from turtle import *

def drawACircle():
    title('Meu primeiro círculo!')
    shape('circle')
    aux = 0
    item = 0

    begin_fill()

    while aux < 24:
        item = item + 15
        setheading(item)
        fd(150)
        write(item)
        bk(150)
        aux = aux+1

    end_fill()

    done()

drawACircle()