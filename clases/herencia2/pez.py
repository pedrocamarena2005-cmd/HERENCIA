from clases.herencia2.animal import Animal


class Pez(Animal):
    def __init__(self, especie, nombre, aletas):
        super().__init__(especie, nombre)
        self.aletas = aletas

    def __str__(self):
        return super().__str__() + " " + str(self.aletas)

    def nadar(self):
        print("Nadando...")
