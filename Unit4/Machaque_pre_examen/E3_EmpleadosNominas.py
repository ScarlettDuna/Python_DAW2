class Documento:
    def __init__(self, numero, letra = 'X'):
        self.numero = numero
        self.letra = letra

    @property
    def numero(self):
        return self._numero
    @numero.setter
    def numero(self, numero):
        if isinstance(numero, str) and len(numero) == 8:
            self._numero = numero
        else:
            raise ValueError("Debe ser un texto de 8 dígitos")

    @property
    def letra(self):
        return self._letra
    @letra.setter
    def letra(self, letra = 'X'):
        if isinstance(letra, str) and len(letra) == 1:
            self._letra = letra
        else:
            raise ValueError("Debe ser una sola letra")

    def __str__(self):
        return f"Documento: {self.numero}{self.letra}"

class PersonaEmpresa(Documento):
    def __init__(self, nombre, edad, numero, letra = 'X'):
        super().__init__(numero, letra)
        self.nombre = nombre
        self.edad = edad

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str):
            self._nombre = nombre
        else:
            raise ValueError("Debe ser un texto")

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self._edad = edad
        else:
            raise ValueError("Debe ser un número positivo.")

    def __str__(self):
        return f"Empleado con nombre: {self.nombre} edad: {self.edad} y documento: {self.numero}{self.letra}."

class Nomina:
    def __init__(self):
        self.pagos = {}

    def add_pago(self, concepto, cantidad):
        if isinstance(concepto, str) and isinstance(cantidad, (int, float)) and cantidad > 0:
            self.pagos[concepto] = cantidad
        else:
            raise ValueError("El concepto debe ser un texto y la cantidad un número positivo")
    def mod_pago(self, concepto, cantidad):
        if concepto in self.pagos:
            if isinstance(cantidad, (int, float)) and cantidad > 0:
                self.pagos[concepto] = cantidad
        else:
            raise ValueError("El concepto no existe. No se ha podido modificar el pago.")
    def del_pago(self, concepto):
        if concepto in self.pagos:
            del self.pagos[concepto]
        else:
            raise ValueError("El concepto no existe. No se ha podido borrar el pago.")
    def media(self):
        total = 0
        contador = 0
        for item in self.pagos.values():
            total += item
            contador += 1
        if contador != 0:
            return total / contador
        else:
            raise ValueError("No hay conceptos para calcular la media.")

empleTest1 = PersonaEmpresa("Sergio", 28, "24681357", "S")
empleTest2 = PersonaEmpresa("Marina", 45, "13572468", "M")
