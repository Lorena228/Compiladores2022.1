raiz = {}
opt = 0


def vazio(aux):
    if (len(aux.values()) <= 0):
        return True
    else:
        return False


def inserirArvore(aux, num):
    if (vazio(aux)):
        aux = {"num": num, "esq": {}, "dir": {}}
    elif (num < aux["num"]):
        aux["esq"] = inserirArvore(aux["esq"], num)
    else:
        aux["dir"] = inserirArvore(aux["dir"], num)
    return aux


def mostrarPares(aux):
    if (not vazio(aux)):
        mostrarPares(aux["esq"])
        if (aux["num"] % 2 == 0):
            print(aux["num"], end=" ")
        mostrarPares(aux["dir"])


def mostrarEmOrdem(aux):
    if (not vazio(aux)):
        mostrarEmOrdem(aux["esq"])
        print(aux["num"], end=" ")
        mostrarEmOrdem(aux["dir"])


def mostrarEmPreOrdem(aux):
    if (not vazio(aux)):
        print(aux['num'], end=" ")
        mostrarEmPreOrdem(aux["esq"])
        mostrarEmPreOrdem(aux["dir"])


def mostrarEmPosOrdem(aux):
    if (not vazio(aux)):
        mostrarEmPosOrdem(aux["esq"])
        mostrarEmPosOrdem(aux["dir"])
        print(aux["num"], end=" ")


while (opt != 5):
    print('MENU - ÁRVORE BINÁRIA')
    print('1-Inserir número')
    print('2-Consultar números pares')
    print('3-Consultar toda a arvore em ordem')
    print('4-Esvaziar a árvore')
    print('5-Consultar árvore em pré-ordem')
    print('6-Consultar árvore em pós-ordem')
    print('7-Sair')

    opt = int(input("Digite um dos números acima: "))
    if (1 < opt > 7):
        print("Opção inválida")
    elif (opt == 1):
        raiz = inserirArvore(
            raiz, int(input('Digite o número para inserir na árvore: ')))
    elif (opt == 2):
        if (vazio(raiz)):
            print("Árvore Vazia")
        else:
            mostrarPares(raiz)
    elif (opt == 3):
        if (vazio(raiz)):
            print('Árvore Vazia')
        else:
            mostrarEmOrdem(raiz)
    elif (opt == 4):
        raiz.clear
    elif (opt == 5):
        if (vazio(raiz)):
            print('Árvore Vazia')
        else:
            mostrarEmPreOrdem(raiz)
    elif (opt == 6):
        if (vazio(raiz)):
            print('Árvore Vazia')
        else:
            mostrarEmPosOrdem(raiz)
