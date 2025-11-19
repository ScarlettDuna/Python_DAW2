class Alumno():
    contador = 0
    def __init__(self, nombre=""):
        self.nombre = nombre
        Alumno.contador += 1

alumno1 = Alumno("Pepe")
alumno2 = Alumno("Luis")
alumno3 = Alumno("Jaime")
print("¿Cuántos alumnos hay?: ", Alumno.contador)
# Para ver el nombre debo acceder al objeto, no a la clase
print(f"¿Cómo se llaman? {alumno1.nombre}, {alumno2.nombre} y {alumno3.nombre}.")