from collections import deque
'''pilha = [8, 9, 9]
pilha.append(3)
pilha.append(4)
tela = pilha.pop()
print(tela)
print(pilha)'''

#Lista1 cria uma pilha Fist In Last Out
'''lista = []
def insereLista(valor):
    return lista.append(valor)

def removeLista():
    return lista.pop(0)

for i in range(10):
    insereLista(i)
    print('Lista atualizada:', lista)

for x in range(10):
    x = removeLista()
    print('Lista com pop:', lista)'''

#Lista2 Comandas do Restaurante Exemplo de pilha FIFO
'''lista = []


def insereLista(valor):
    return lista.append(valor)


def removeComanda():
    return lista.pop(0)


for i in range(3):
    x = input('Qual prato deseja pedir?')
    insereLista({'pedido': i, 'prato': x})
    print('Lista de comandas atualizada:', lista)

for j in range(len(lista)):
    x = removeComanda()
    print('Lista de entrega:', x)'''

#Pilha1 Pilha Fist In Last Out (FILO)
'''lista = []


def inserePilha(valor):
    lista.append(valor)


def removePilha():
    return lista.pop(0)


for i in range(10):
    inserePilha(i)
    print("Lista atualizada:", lista)

for i in range(len(lista)):
    x = removePilha()
    print("Número removido:", x)'''
