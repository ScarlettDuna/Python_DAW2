# Encapsulación: convertir métodos en atributos, decoradores
class Circulo():
    def __init__(self, radio):
        self.radio = radio
    # Vamos a usar un decorador @property para convertir un mét6odo en atributo
    # Así podemos acceder a los métodos directamente
    @property
    def radio(self):
        return self._radio
    # Es necesario definir un setter
    @radio.setter
    def radio(self, radio):
        if radio >= 0:
            self._radio = radio
        else:
            self._radio = 0
            raise ValueError("Radio debe ser positivo")
    @radio.deleter
    def radio(self):
        del self._radio

    # Podemos reescribir los métodos que proporciona la clase
    def __str__(self):
        clase = type(self).__name__
        msg = "{0} de radio {1}"
        return msg.format(clase, self.radio)
    # Otra forma de representar un objeto para depurar y desarrollo
    def __repr__(self):
        clase = type(self).__name__
        msg = "{0}({1})"
        return msg.format(clase, self.radio)
    # Puedo reescribir el método para comparar objetos
    def __eq__(self, otro):
        return self.radio == otro.radio
    # Puedo determinar como se suman cículos
    def __add__(self, otro):
        self.radio += otro.radio

circ1 = Circulo(5)
print(circ1)
print(repr(circ1))
# Otro círculo
circ2 = Circulo(7)
print(circ1==circ2)
circ1+circ2
print(circ1)