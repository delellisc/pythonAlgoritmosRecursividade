def bubbleSort(lista):
    i = 0
    while i < len(lista)-1:
        j = 0
        while j < len(lista)-i-1:
            if(lista[j] > lista[j+1]):
                tmp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = tmp
            j += 1
        i += 1

# ***********************************************
# teste
lista = [2, 8, 5, 3, 9, 4, 1]
print(lista) # [2, 8, 5, 3, 9, 4, 1]
bubbleSort(lista)
print(lista) # [1, 2, 3, 4, 5, 8, 9]