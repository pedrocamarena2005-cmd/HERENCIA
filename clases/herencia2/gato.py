from clases.herencia2.animal import Animal


class Gato(Animal):
    def __init__(self, especie, nombre, velocidad):
        super().__init__(especie, nombre)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + " " + str(self.velocidad)

    def maullar(self):
        print("Maullando...")
