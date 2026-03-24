from clases.industrial.maquina import Maquina


class Torno(Maquina):
    def __init__(self, nombre, codigo, consumoEnergia, diametroMaximoPieza, estado="apagada"):
        super().__init__(nombre, codigo, consumoEnergia, estado)
        self.diametroMaximoPieza = diametroMaximoPieza

    def iniciarMecanizado(self):
        return "Proceso de mecanizado iniciado"

    def mostrarInformacion(self):
        return (
            f"{super().mostrarInformacion()}\n"
            f"Diametro maximo de pieza: {self.diametroMaximoPieza} cm"
        )
