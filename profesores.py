#referencia de la clase
from clases.personas import persona

class Profesor(Persona):

    def __init__(self):
        super().__init__()
        self.clave = ""


    def leerDatosProfesor(self):
        self.clave = imput("Clave profesor: ")
    
    def mostrarDatosProfesor(self):
        print(self.clave)