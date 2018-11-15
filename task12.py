import turtle

lado = int(input('Insira o tamanho do lado do círculo: \n'))

def circulo(number):
    for i in range(4):
        turtle.circle(number)
        turtle.right(90)
        
circulo(lado)