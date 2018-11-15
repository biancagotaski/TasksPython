from turtle import *

lados = int(input('Quantos lados o seu polígono deve ter? \n'))

##this can do better
def draw(nlados):
    
    begin_fill()
    color('blue', 'yellow') ##only shows the second color in shape
    delay(15)
    
    anguloExterno = 360 / nlados
    comprimento = 600 / nlados
    penup()
    goto(-comprimento / 2, -comprimento / 2)
    pendown()
    for i in range(0, nlados):
        forward(comprimento)
        left(anguloExterno)
    hideturtle()
    draw(lados)
    
end_fill()

draw(lados)