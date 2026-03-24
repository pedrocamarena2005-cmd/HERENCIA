from clases.industrial.prensa_hidraulica import PrensaHidraulica
from clases.industrial.torno import Torno


def main():
    torno = Torno("Torno CNC", "M001", 15, 50)
    prensa = PrensaHidraulica("Prensa Hidraulica", "M002", 20, 100)

    torno.encender()
    prensa.encender()

    print(torno.mostrarInformacion())
    print(torno.iniciarMecanizado())
    torno.apagar()
    print()
    print(prensa.mostrarInformacion())
    print(prensa.iniciarPrensado())
    prensa.apagar()


if __name__ == "__main__":
    main()
