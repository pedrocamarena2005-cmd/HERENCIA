from clases.herencia1.vehiculo import Vehiculo


class Taxi(Vehiculo):
    def __init__(self, matricula, modelo, potenciaCV, numeroLicencia):
        super().__init__(matricula, modelo, potenciaCV)
        self.numeroLicencia = numeroLicencia

    def __str__(self):
        return super().__str__() + " " + str(self.numeroLicencia)

    def subirPasajeros(self):
        print("Subiendo pasajeros...")

    def cobrarCuota(self):
        print("Cobrando cuota...")
