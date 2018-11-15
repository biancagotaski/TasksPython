import turtle

def draw():
    for i in range(4):
        makeSquad()
        turtle.fd(100)
        
def makeSquad():
    for i in range(4):
        turtle.fd(100)
        turtle.left(90)

draw()