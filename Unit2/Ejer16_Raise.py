# Lanzar excepciones
def validar_edad(edad):
    # primero validamos que es un número entero
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero")
    if not 0 < edad < 120:
        raise ValueError("La edad debe estar entre 1 y 119")
    return edad

try:
    mi_edad = validar_edad(30)
    print(f"Tu edad es {mi_edad}")
except (TypeError, ValueError) as e:
    print(f"Error al obtener la edad: {e}")