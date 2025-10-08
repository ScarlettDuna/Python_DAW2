# Ejemplo de uso de excepciones else
try:
    num = int(input("Introduce un número"))
except ValueError:
    print("Entrada inválida, debe ser un número")
else:
    print(f"El número introducido es: {num}")
    print("No se ha producido excepción")