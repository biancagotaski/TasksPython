import turtle

lado = int(input('Insira o tamanho do lado do quadrado: \n'))

def triangulo(number):
    for i in range(3):
        turtle.fd(number)
        turtle.right(120)
        
triangulo(lado)