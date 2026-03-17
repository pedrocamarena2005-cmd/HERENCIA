class Animal(object):
    def __init__(self, especie, nombre):
        self.especie = especie
        self.nombre = nombre

    def __str__(self):
        return self.especie + " " + self.nombre

    def respirar(self):
        print("Respirando...")
