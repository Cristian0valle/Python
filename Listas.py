lista1 = ["uno", "dos", "tres"]

print(lista1[2])

lista1.append("cuatro") # .append agrega un elemento a la lista en la ultima posicion
lista1.append("cinco")

lista1.pop(4) #elimina el elemento enviado en el parametro

print(len(lista1)) #len cuenta la cantidad de elementos de la lista

for x in lista1:
    print(x)
