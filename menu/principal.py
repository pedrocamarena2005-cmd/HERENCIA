import sys
from pathlib import Path

# Permite importar figuras.py cuando se ejecuta este archivo directamente.
sys.path.append(str(Path(__file__).resolve().parents[1]))

from figuras import Circulo, Triangulo


def mostrar_menu():
    print("\n=== MENÚ FIGURAS ===")
    print("1. Capturar Círculo")
    print("2. Capturar Triángulo")
    print("3. Mostrar Círculo")
    print("4. Mostrar Triángulo")
    print("5. Cargar caso de prueba")
    print("0. Salir")


def cargar_caso_prueba():
    circulo = Circulo("Círculo", "Azul", 5)
    triangulo = Triangulo("Triángulo", "Verde", 10, 8)
    return circulo, triangulo


def main():
    circulo = None
    triangulo = None

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            circulo = Circulo()
            print("\nIngresa datos del Círculo")
            circulo.leer()
            print("Círculo guardado.")
        elif opcion == "2":
            triangulo = Triangulo()
            print("\nIngresa datos del Triángulo")
            triangulo.leer()
            print("Triángulo guardado.")
        elif opcion == "3":
            if circulo:
                circulo.mostrar_datos()
            else:
                print("Aún no hay datos de Círculo.")
        elif opcion == "4":
            if triangulo:
                triangulo.mostrar_datos()
            else:
                print("Aún no hay datos de Triángulo.")
        elif opcion == "5":
            circulo, triangulo = cargar_caso_prueba()
            print("Caso de prueba cargado correctamente.")
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
