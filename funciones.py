'''
Parametros = variables
argumentos = valor
'''

def suma(x,y):
    print(x+y)

def resta(x,y):
    print(x-y)

def multiplicacion(x,y):
    print(x*y)

def division(x,y):
    print(x/y)


def Nombre(nombre="cristian"):
    print("Hola " + nombre)

print(suma(3,5)) #pasamos los argumentos necesarios
print(resta(3,5))
print(multiplicacion(3,5))
print(division(3,5))

print(Nombre()) #si no le paso ningun argumento me entrega el valor asignado anteriormente
print(Nombre("Camila"))