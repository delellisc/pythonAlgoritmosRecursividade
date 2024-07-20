import random
import time

#************************************************

def binarySearch(lista, x):
    inicio = 0
    fim = len(lista)
    while inicio < fim: # se o índice do "ínicio" não estiver mais à esquerda do "fim", significa que a lista não contém o valor
        meio = (inicio + fim)//2
        if lista[meio] == x: # o loop é executado até o item no meio da lista ser equivalente ao elemento desejado
            return True
        elif lista[meio] < x: # como o x é maior do que o valor no meio da lista, a parte da direita deve ser vasculhada
            inicio = meio + 1
        else: # como o x é menor do que o valor no meio da lista, a parte da esquerda deve ser vasculhada
            fim = meio
    return False

#************************************************

def recursiveBinarySearch(lista, x, inicio, fim):
    if inicio < fim: # se o índice do "ínicio" não estiver mais à esquerda do "fim", significa que a lista não contém o valor
        meio = (inicio + fim)//2
        if lista[meio] == x: # enquanto x não for igual ao elemento no meio da lista , a função será chamada recursivamente
            return True
        elif lista[meio] < x: # chama recursivamente a função, vasculhando apenas a parte da direita
            return recursiveBinarySearch(lista, x, meio + 1, fim)
        else: # chama recursivamente a função, vasculhando apenas a parte da esquerda
            return recursiveBinarySearch(lista, x, inicio, meio)
    else:
        return False

#************************************************

i = 0
lista = []
while i < 1000000:
    lista.append(random.randint(1,100))
    i += 1

numero = random.randint(1, 100)

start = (time.time())
binarySearch(lista, numero)
stop = (time.time())
print(stop - start)

start = (time.time())
recursiveBinarySearch(lista, numero, 0, len(lista))
stop = (time.time())
print(stop - start)