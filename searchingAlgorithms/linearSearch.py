def linearSearch(lista, x):
    i = 0
    while i < len(lista):
        if x == lista[i]:
            return True
        i += 1
    return False
#************************************************
# teste
lista = [5, 4, 10, 2, 25, 13, 0, 7]
if linearSearch(lista, 10): # saída: Encontrado
    print("Encontrado")
else:
    print("Não encontrado")
if linearSearch(lista, 77): # saída: Não encontrado
    print("Encontrado")
else:
    print("Não encontrado")