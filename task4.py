number = int(input("insira o valor de n para fatorar: \n"))

def calculateFactorial(n):
    fact = 1
    i = 2
    while i <= n:
        fact = fact*i
        i += 1
    print('O fatorial de n ', n, 'é: ', fact)
            
calculateFactorial(number) 