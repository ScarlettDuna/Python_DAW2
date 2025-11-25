# Encapsulación: convertir métodos en atributos, decoradores
class Circulo():
    def __init__(self, radio):
        self.radio = radio
    # Vamos a usar un decorador @property para convertir un mét6odo en atributo
    # Así podemos acceder a los métodos directamente
    @property
    def radio(self):
        print("Estoy dando el radio en un método con decorador")
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

circ1 = Circulo(5)
print("El radio es: ", circ1.radio)
circ1.radio = 8
print("El radio es: ", circ1.radio)
# borramos el atributo
del circ1.radio
print("El radio es: ", circ1.radio)