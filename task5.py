tupleColor = ('red','purple','blue','green','orange','yellow')

option = input('Escolha qual tarefa deseja exibir o resultado:\n1- Tarefa 1\n2- Tarefa 2\n3- Tarefa 3\n4- Tarefa 4\n')

def checkEachTask():    
    if option == '1':
        checkIndexOfTuple()
    elif option == '2':
        checkHalfTuple()
    elif option == '3':
        removeItemFromTuple()
    elif option == '4':
        newTuple()
    else:
        print('Opção inválida. Tente novamente.')

####Task 1
def checkIndexOfTuple():
     if 'green' in tupleColor:
         index = str(tupleColor.index('green'))
         print('O índice do elemento da tupla é: ' + index)
     else:
         print('Elemento não existe na tupla')

####Task 2
def checkHalfTuple():
    index_half = int(len(tupleColor) / 2)
    half1 = (tupleColor[:index_half])
    half2 = (tupleColor[index_half:])
    
    print(half1)
    print(half2)

####Task 3
####THIS IS A JOKE TASK, BECAUSE THE TUPLES ARE IMMUTABLE
def removeItemFromTuple():
    tuplex = list(tupleColor)
    #retira a cor azul da tupla
    tuplex.pop(2)
    tupleColorUpdated = tuple(tuplex)
    print(tupleColorUpdated)

####Task 4  
def newTuple():
    newTuple = ()
    for i in reversed(tupleColor):
        newTuple = newTuple + (i,)
    print(newTuple)
    
        
checkEachTask()