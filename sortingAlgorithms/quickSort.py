def partition(lista, inicio, fim):
    pivo = lista[fim]
    i = (inicio-1)
    j = inicio
    while j <= (fim - 1):
        if lista[j] < pivo:
            i += 1
            tmp = lista[i]
            lista[i] = lista[j]
            lista[j] = tmp
        j += 1
    tmp = lista[i + 1]
    lista[i + 1] = lista[fim]
    lista[fim] = tmp
    return (i + 1)
def quickSort(lista, inicio, fim):
    if inicio < fim:
        pivo = partition(lista, inicio, fim)
        quickSort(lista, inicio, pivo - 1)
        quickSort(lista, pivo + 1, fim)
#************************************************
# teste
lista = [2, 8, 5, 3, 9, 4, 1]
print(lista)
quickSort(lista, 0, len(lista) - 1)
print(lista)
