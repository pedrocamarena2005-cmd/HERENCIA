class Maquina(object):
    def __init__(self, nombre, codigo, consumoEnergia, estado="apagada"):
        self.nombre = nombre
        self.codigo = codigo
        self.consumoEnergia = consumoEnergia
        self.estado = estado

    def encender(self):
        self.estado = "encendida"

    def apagar(self):
        self.estado = "apagada"

    def mostrarInformacion(self):
        return (
            f"Maquina: {self.nombre}\n"
            f"Codigo: {self.codigo}\n"
            f"Consumo de energia: {self.consumoEnergia} kWh\n"
            f"Estado: {self.estado.capitalize()}"
        )
