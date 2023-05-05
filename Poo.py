class Coche:
    """
        Abstraccion de los objetos coche.
    """
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print("Tenemos" , gasolina, "litros")

    def arrancar(self):
        if self.gasolina > 0:
             print("Partio mierda")
        else:
            print("Ta en pana")

    def conducir(self):
        if self.gasolina > 0:
              self.gasolina -= 1
              print("Quedan... ", self.gasolina, "Litros" )
        else:
            print("No se mueve")

micoche = Coche(5)  

micoche.arrancar()
micoche.conducir()


class Instrumentos:
    """
        Abstraccion de los objetos instrumentos
    """
    def __init__(self, precio):
        self.precio = precio

    def tocar(self):
        print("ROCKANROOLL BEIBI")
    def romper(self):
        print("Tendras que comprarte otro")
        print("Son: ", self.precio, "$")

class bateria(Instrumentos):
    pass

class bajo(Instrumentos):
    pass


Guitarra = Instrumentos(800000)
Guitarra.tocar()
Guitarra.romper()

Bateria1 = bateria(6444)
bateria.tocar()
    












