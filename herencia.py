'''Aqui se explica el concepto de la herencia de la programacion Orientada a objetos,
donde la clase hijo heredara los atributos y metodos de la clase padre
'''

class ClasePadre:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print("Hola, soy", self.nombre)


class ClaseHijo(ClasePadre):
    def __init__(self, nombre, edad):
        super().__init__(nombre)  # Llamada al constructor de la clase padre
        self.edad = edad

    def saludar(self):
        super().saludar()  # Llamada al método de la clase padre
        print("Tengo", self.edad, "años.")


# Crear una instancia de la clase hija
objeto_hijo = ClaseHijo("Cristian", 25)

# Acceder a los atributos y métodos de la clase padre
print(objeto_hijo.nombre) 
objeto_hijo.saludar()