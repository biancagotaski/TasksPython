import turtle

lado = int(input('Insira o tamanho do lado do quadrado: \n'))

def quadrado(number):
    for i in range(4):
        turtle.fd(number)
        turtle.right(90)
        
quadrado(lado)