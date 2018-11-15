import turtle

lado = int(input('Insira o tamanho do lado do quadrado: \n'))

def quadrado():
    for i in range(4):
        turtle.fd(lado)
        turtle.right(90)

def desenhaQuadrados():
    nQuadrados = int(input('Quantos quadrados deseja desenhar?'))
    
    for i in range(nQuadrados):
        quadrado()
        turtle.left(900)
        turtle.penup()
        turtle.forward(50)
        turtle.right(90)
        turtle.pendown()
    
desenhaQuadrados()