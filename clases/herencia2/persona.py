class Persona(object):
    def __init__(self, clave, nombre, edad):
        self.clave = clave
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return self.clave + " " + self.nombre + " " + str(self.edad)
