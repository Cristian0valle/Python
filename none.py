'''
None es un valor especial que se utiliza para 
representar la ausencia de un valor o la falta de definición de una variable.
'''

def saludar(nombre=None):
    if nombre is None:
        print("Hola, ¿cómo estás?")
    else:
        print("Hola,", nombre)

saludar()  # Salida: Hola, ¿cómo estás?
saludar("Cristian")  # Salida: Hola, Cristian