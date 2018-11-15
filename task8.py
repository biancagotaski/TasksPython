x = int(input('Informe o valor de x: \n'))
y = int(input('Informe o valor de y: \n'))
z = int(input('Informe o valor de z: \n'))

tuple = (x, y, z)

def calculateTriangle():
    if x < y + z or y < x + z or z < x + y:
        print('Triângulo formado :)')
        if x == y == z:
            print('O triângulo é do tipo Equilátero!')
        elif x == y or x == z or y == z:
            print('O triângulo é do tipo Isósceles!')
        elif x != y and x != z and y != z:
            print('O triângulo é do tipo Escaleno!')
        else:
            print('Não é possível formar um triângulo com os valores informados. Tente novamente.')
     
    return x, y, z
    
calculateTriangle()