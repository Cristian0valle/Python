diccionario1 = {
    "clave1": "primer valor",
    "segunda clave": "segundo valor",
    "tercera clave": "tercer valor",
    "cuarta clave": "cuarto valor"
}

diccionarioAnidado ={
    "primerDiccionario": {
    "nombre":"cristian",
    "apellido": "ovalle",
    "numero": 123432
},
 "segundoDiccionario": {
    "nombre":"Anakin",
    "apellido": "Skywalker",
    "numero": 123432
}
}

#obtener valores
print(diccionario1["clave1"])

print(diccionario1.get("clave1"))

#cambiar valor a un elemento
diccionario1["cuarta clave"] = "quinto valor"

#agregar un elemento al diccionario

diccionario1["quinta clave"] = "quinto valor 2"

#eliminar un elemento
diccionario1.pop("quinta clave")


#eliminar ultimo elemento agregado popitem()
#diccionario1.popitem()

#Vaciar diccionario
#diccionario1.clear()

#recorrer las claves
for x in diccionario1:
    print(x)


#recorrer solo los valores
for x in diccionario1.values():
    print(x)

#recorrer clave como valores
for x,y in diccionario1.items():
    print(x,y)