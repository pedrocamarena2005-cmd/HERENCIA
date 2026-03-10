from clases.herencia1.taxi import Taxi


def main():
    coche = Taxi("123-GTO", "Versa", 1000, "123-a")
    print(coche)
    coche.encender()
    coche.subirPasajeros()
    coche.acelerar()
    coche.frenar()
    coche.cobrarCuota()


if __name__ == "__main__":
    main()
