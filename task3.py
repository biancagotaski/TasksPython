inputUser = input("insira o valor de n para fatorar: \n")
number = int(inputUser)

def calculateFactorial(n):
    fact = 1
    if n < 0:
        print('O fatorial de zero é 1')
    else:
        for i in range(1, n+1):
            fact = fact * i
        print('O fatorial de ',n, 'é: ', fact)
            
calculateFactorial(number) 