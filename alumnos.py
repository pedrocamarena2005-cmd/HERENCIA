#crear la referencia
from clases.personas import Persona

class Alumno(Persona):
    def __init__(self):
        self.cuenta = ""

    def leerDatosAlumno(self):
        self.cuenta = input("Cuenta: ")
    
    def mostrardatosAlumno(self):
        print(self.cuenta):