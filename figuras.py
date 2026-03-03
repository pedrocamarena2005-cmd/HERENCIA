import math


class Figura:
    def __init__(self, nombre="", color=""):
        self.nombre = nombre
        self.color = color


class Circulo(Figura):
    def __init__(self, nombre="", color="", radio=0.0):
        super().__init__(nombre, color)
        self.radio = radio

    def leer(self):
        self.nombre = input("Forma: ").strip()
        self.color = input("Color: ").strip()
        self.radio = float(input("Radio: "))

    def calcular_area(self):
        return round(math.pi * (self.radio ** 2), 2)

    def mostrar_datos(self):
        print("\nCírculo")
        print(f"Forma: {self.nombre}")
        print(f"Color: {self.color}")
        print(f"Radio: {self.radio:g}")
        print(f"Área: {self.calcular_area()}")


class Triangulo(Figura):
    def __init__(self, nombre="", color="", base=0.0, altura=0.0):
        super().__init__(nombre, color)
        self.base = base
        self.altura = altura

    def leer(self):
        self.nombre = input("Forma: ").strip()
        self.color = input("Color: ").strip()
        self.base = float(input("Base: "))
        self.altura = float(input("Altura: "))

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def mostrar_datos(self):
        area = self.calcular_area()
        area_txt = str(int(area)) if area == int(area) else str(area)

        print("\nTriángulo")
        print(f"Forma: {self.nombre}")
        print(f"Color: {self.color}")
        print(f"Base: {self.base:g}")
        print(f"Altura: {self.altura:g}")
        print(f"Área: {area_txt}")
