def insertionSort(lista):
    i = 0
    while i < len(lista):
        j = i
        while j > 0:
            if lista[j] < lista[j-1]:
                tmp = lista[j]
                lista[j] = lista[j-1]
                lista[j-1] = tmp
            j -= 1
        i += 1
#************************************************
# teste
lista = [2, 8, 5, 3, 9, 4]
print(lista) # [2, 8, 5, 3, 9, 4]
insertionSort(lista)
print(lista) # [2, 3, 4, 5, 8, 9]
