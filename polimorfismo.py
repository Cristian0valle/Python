'''
El polimorfismo es un concepto en la Poo, que permite que objetos de diferentes clases 
se comporten de manera similar al recibir el mismo mensaje o al invocar el mismo método
'''

class Animal:
    def sonido(self):
        pass


class Perro(Animal):
    def sonido(self):
        print("El perro ladra")


class Gato(Animal):
    def sonido(self):
        print("El gato maulla")


def Rugir(animal):
    animal.sonido()


perro = Perro()
gato = Gato()


Rugir(perro)  # Salida: El perro ladra
Rugir(gato)  # Salida: El gato maulla