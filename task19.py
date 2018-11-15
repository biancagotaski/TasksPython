from turtle import *
 
value = int(input('Insira a quantidade de voltas: \n'))
 
def makeDraw():
     color('red')

     shape('turtle')
 
     for x in range(value):
        forward(x)
        left(90)
        speed(15)
        
makeDraw()