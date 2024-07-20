def shellSort(lista):
    intervalo = len(lista)//2
    while intervalo >= 1:
        i = 0
        while i < len(lista):
            tmp = lista[i]
            j = i
            while j >= intervalo and lista[j-intervalo] > tmp:
                lista[j] = lista[j-intervalo]
                j -= intervalo
            lista[j] = tmp
            i += 1
        intervalo //= 2
#************************************************
# teste
lista = [2, 8, 3, 4, 9, 10, 5, 7]
print(lista) # [2, 8, 3, 4, 9, 10, 5, 7]
shellSort(lista)
print(lista) # [2, 3, 4, 5, 7, 8, 9, 10]
