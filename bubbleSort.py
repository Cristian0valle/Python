def bubble_sort(lista):
    n = len(lista)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                # Realizar intercambio
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

numeros = [7, 3, 9, 2, 1, 5]
numeros_ordenados = bubble_sort(numeros)
print("Lista ordenada:", numeros_ordenados)