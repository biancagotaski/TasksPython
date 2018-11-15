import turtle

turtle.title("Utilizando nossas Funções!")

def quadrado():
    for i in range(4):
        turtle.fd(100)
        turtle.right(90)
        
def triangulo():
    for i in range(3):
        turtle.fd(100)
        turtle.right(120)

def circulo():
    turtle.circle(100)
    turtle.right(90)

def next():
    penup()
    forward(100)

turtle.listen()

turtle.onkey(quadrado, 'q')
turtle.onkey(triangulo, 't')
turtle.onkey(circulo, 'c')
turtle.onkey(next, 'n')

