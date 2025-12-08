class DNIARG:
    def __init__(self, numero):
        self.numero = numero
        self.letra = "A"
    # Getter y Setter - numero
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, numero):
        if isinstance(numero, str) and len(numero) == 8:
            self._numero = numero
        else:
            raise ValueError ("El número debe ser introducido como texto")
        
    def __str__(self):
        return f"El DNI es {self.numero}{self.letra}"
    
class PersonaARG(DNIARG):
    def __init__(self, numero, nombre, edad):
        super().__init__(numero)
        self.nombre = nombre
        self.edad = edad
    # Getter y Setter - nombre   
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str):
            self._nombre = nombre
        else:
            raise ValueError ("El nombre debe ser introducido como texto")
    # Getter y Setter - nombre
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self._edad = edad
        else:
            raise ValueError ("La edad debe ser un número positivo")
        
    def __str__(self):
        return f"Esta persona se llama {self.nombre} y tiene {self.edad} años con DNI {self.numero}{self.letra}."
        
class NotasARG:
    def __init__(self):
        self.notas = {}
        
    def addnotas(self, asignatura, nota):
        if isinstance(asignatura, str) and nota >= 0:
            self.notas[asignatura] = nota
        else:
            raise ValueError ("La asignatura debe ser un texto y la nota un número positivo")
        
    def modnotas(self, asignatura, nota):
        if asignatura in self.notas and nota >= 0:
            self.notas[asignatura] = nota
        else:
            raise ValueError ("No se ha encontrado la asignatura o el número introducido no es positivo")
        
    def delnotas(self, asignatura):
        if asignatura in self.notas:
            del self.notas[asignatura]
        else:
            raise ValueError("No se ha encontrado la asignatura")

    def media(self):
        contador = 0
        total = 0
        for item in self.notas.values():
            total += item
            contador += 1
        if contador != 0:
            return total / contador
        else:
            return 0
        
    def __str__(self):
        return str(self.notas)
    
class AlumnoARG(PersonaARG, NotasARG):
    def __init__(self, numero, nombre, edad):
        PersonaARG.__init__(self, numero, nombre, edad)
        NotasARG.__init__(self)
        
            
print("Uso de persona")
miPersona = PersonaARG("12345678", "Arantxa", 23)
print(miPersona)
print("Uso de notas")
miNota = NotasARG()
miNota.addnotas("matematicas", 5.2)
print(miNota)
miNota.addnotas("lengua", 7)
print(miNota)
print("Modificar nota")
miNota.modnotas("matematicas", 8)
print(miNota)
#Alumno
print("Uso de Alumno")
unAlumno = AlumnoARG("12345678", "Arantxa" , 22)
print(unAlumno)
unAlumno.addnotas("dibujo", 5.8)
unAlumno.addnotas("sociales", 9.0)
print("La media es ", unAlumno.media())
