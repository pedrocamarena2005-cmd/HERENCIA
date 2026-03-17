from clases.herencia1.vehiculo import Vehiculo


class AutoParticular(Vehiculo):
    def __init__(self, matricula, modelo, potenciaCV, numeroPlazas):
        super().__init__(matricula, modelo, potenciaCV)
        self.numeroPlazas = numeroPlazas

    def __str__(self):
        return super().__str__() + " " + str(self.numeroPlazas)

    def pasear(self):
        print("Paseando...")

    def irAlSuper(self):
        print("Yendo al super...")
