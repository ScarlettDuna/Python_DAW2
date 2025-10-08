class ErrorCantidadInvalida(Exception):
    def __init__(self, cantidad, mensaje="La cantidad debe ser positiva"):
        self.cantidad = cantidad
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def procesar_pago(cantidad):
    print("Procesando el pago: ", cantidad)
    if cantidad <= 0:
        raise ErrorCantidadInvalida(cantidad)
    print("Pago procesado correctamente")

try:
    procesar_pago(100)
    # procesar_pago("aaabbb")
    procesar_pago(0)
except ErrorCantidadInvalida as e:
    print(e)
except ValueError as e:
    print(e)