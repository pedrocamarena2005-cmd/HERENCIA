from clases.industrial.maquina import Maquina


class PrensaHidraulica(Maquina):
    def __init__(self, nombre, codigo, consumoEnergia, fuerzaPrensado, estado="apagada"):
        super().__init__(nombre, codigo, consumoEnergia, estado)
        self.fuerzaPrensado = fuerzaPrensado

    def iniciarPrensado(self):
        return "Proceso de prensado iniciado"

    def mostrarInformacion(self):
        return (
            f"{super().mostrarInformacion()}\n"
            f"Fuerza de prensado: {self.fuerzaPrensado} toneladas"
        )
