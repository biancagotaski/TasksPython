word = str(input('Insira a palavra que será rotacionada: \n'))
num = int(input('Insira a quantidade de vezes em que a palavra será rotacionada: \n'))

def rotationString():
    if word != 0:
       word_rotation = word[num:] + word[:num]
       print(word_rotation)
    

rotationString()