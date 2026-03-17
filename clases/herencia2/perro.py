from clases.herencia2.animal import Animal


class Perro(Animal):
    def __init__(self, especie, nombre, fuerzaMordida):
        super().__init__(especie, nombre)
        self.fuerzaMordida = fuerzaMordida

    def __str__(self):
        return super().__str__() + " " + str(self.fuerzaMordida)

    def ladrar(self):
        print("Ladrando...")
