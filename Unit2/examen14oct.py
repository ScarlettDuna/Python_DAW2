class ImporteInvalidoError(Exception):
    def __init__(self, cantidad, mensaje="El importe del préstamo de"
                                         ""
                                         "be ser entre 1.000€ y 50.000€"):
        self.cantidad = cantidad
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def validacion_monto(cantidad):
    print("Validando si se cumples las condiciones para el préstamo")
    if cantidad < 1_000:
        raise ImporteInvalidoError(cantidad, "La cantidad mínima es de 1.000€")
    elif cantidad > 50_000:
        raise ImporteInvalidoError(cantidad, "La cantidad máxima es de 50.000€")
    return True
validando = True
while validando:
    try:
        monto_prestamo = int(input("Ingrese el importe del préstamo deseado (entre 1.000 y 50.000€): " ))
        validacion_monto(monto_prestamo)
    except ValueError as e:
        print("Error de formato: Debe introducir solo números")
        print("_____________________________________ \n")
    except ImporteInvalidoError as e:
        print(f"Error de negocio: {e}")
        print("_____________________________________ \n")
    else:
        if validacion_monto(monto_prestamo): print(f"Éxito: solicitud de {monto_prestamo}€ procesada \n")
        validando = False
    finally:
        print("Sistema de validación de préstamos terminado")