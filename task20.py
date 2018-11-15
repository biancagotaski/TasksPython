import turtle

lengthSquare = int(input('Insira o comprimento: \n'))

degree = int(input('Insira o número de graus para a rotação do desenho: \n'))

def draw():
    turtle.color('red', 'light green')

    for i in range(lengthSquare):
        turtle.fd(lengthSquare)
        turtle.lt(90 + degree)
        turtle.speed(15)

draw()