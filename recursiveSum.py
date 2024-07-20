def somaRecursiva(x):
    if x <= 0:
        return x
    return x + somaRecursiva(x - 1)

print(somaRecursiva(5)) # saída: 5