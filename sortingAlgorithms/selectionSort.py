def selectionSort(lista):
    i = 0
    while i < len(lista)-1:
        minPosicao = i;
        j = i
        while j < len(lista):
            if lista[j] < lista[minPosicao]:
                minPosicao = j
            j += 1
        if i != minPosicao:
            tmp = lista[i]
            lista[i] = lista[minPosicao]
            lista[minPosicao] = tmp
        i += 1
#************************************************
# teste
lista = [2, 8, 5, 3, 9, 4, 1]
print(lista) # [2, 8, 5, 3, 9, 4, 1]
selectionSort(lista)
print(lista) # [1, 2, 3, 4, 5, 8, 9]