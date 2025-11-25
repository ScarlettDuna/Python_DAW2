class Circulo():
    def __init__(self, radio):
        self.set_radio(radio)
    def set_radio(self, radio):
        # indicamos el atributo _radio con _ por convención para indicar que es privado
        if radio >= 0:
            self._radio = radio
        else:
            self._radio = 0
            raise ValueError("El radio debe ser positivo")
    def get_radio(self):
        print("Estoy devolviendo el radio")
        return self._radio

circ1 = Circulo(10)
print("El radio es: ", circ1.get_radio())
circ2 = Circulo(-245)
print("El radio es: ", circ2.get_radio())