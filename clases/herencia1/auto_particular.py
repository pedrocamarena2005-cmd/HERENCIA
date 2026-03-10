from clases.herencia1.vehiculo import Vehiculo


class AutoParticular(Vehiculo):
    def __init__(self, matricula, modelo, potenciaCV, propietario):
        super().__init__(matricula, modelo, potenciaCV)
        self.propietario = propietario

    def __str__(self):
        return super().__str__() + " " + str(self.propietario)

    def abrirCajuela(self):
        print("Abriendo cajuela...")

    def tocarClaxon(self):
        print("Tocando claxon...")
