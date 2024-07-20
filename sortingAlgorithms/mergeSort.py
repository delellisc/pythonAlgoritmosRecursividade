def merge(lista, inicio, fim, meio):
  listaCopia = [None] * (len(lista))
  i = k = inicio
  j = meio + 1
  while i <= meio and j <= fim:
    if lista[i] < lista[j]:
      listaCopia[k] = lista[i]
      k += 1
      i += 1
    else:
      listaCopia[k] = lista[j]
      k += 1
      j += 1
  while i <= meio:
    listaCopia[k] = lista[i]
    k += 1
    i += 1
  i = inicio
  while i < k:
    lista[i] = listaCopia[i]
    i += 1

def mergeSort(lista, inicio, fim):
  if inicio < fim:
    meio = (inicio + fim) // 2
    mergeSort(lista, inicio, meio)
    mergeSort(lista, meio + 1, fim)
    merge(lista, inicio, fim, meio)

# **********************************************
# teste
lista = [2, 8, 5, 3, 9, 4, 1]
print(lista) # [2, 8, 5, 3, 9, 4, 1]
mergeSort(lista, 0, len(lista) - 1)
print(lista) # [1, 2, 3, 4, 5, 8, 9]