#referencias de clase
from clases.alumnos import Alumnos
from clases.prefesores import Profesor

def main():
    #crear objeto de la clase
    al = Alumno()
    al.leerDatosPersona()
    al.leerDatosAlumno()
    al.mostrarDatosPersona()
    al.mostrarDatosAlumno()

    prof = profesor()
    prof.leerDatosProfesor()
    prof.mostrarDatosProfesor()

if __name__ == "__main__":
    main()