numbers = []
count = 0
firstValue = int(input("Insira o primeiro numero: \n"))
secondValue = int(input("Insira o segundo numero: \n"))
thirdValue = int(input("Insira o terceiro numero: \n"))
numbers.append(firstValue)
numbers.append(secondValue)
numbers.append(thirdValue)

for number in numbers:
    if not number % 2 == 0:
        count += number
        
print("A soma dos numeros impares eh: ", count)
