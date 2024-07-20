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
# teste
lista = [2, 3, 5, 6, 8, 9, 10, 12]

if binarySearch(lista, 12): # saída: Encontrado
    print("Encontrado")
else:
    print("Não encontrado")
if binarySearch(lista, 15): # saída: Não encontrado
    print("Encontrado")
else:
    print("Não encontrado")
if recursiveBinarySearch(lista, 8, 0, len(lista)): # saída: Encontrado
    print("Encontrado")
else:
    print("Não encontrado")
if recursiveBinarySearch(lista, 44, 0, len(lista)): # saída: Não encontrado
    print("Encontrado")
else:
    print("Não encontrado")