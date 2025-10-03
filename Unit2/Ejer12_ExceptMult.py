# Varias excepciones
try:
    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce otro número: "))
    resultado = num1/num2
    print(f"El resultado es {resultado}")
except ValueError:
    print("Error: debe ser un número")
except ZeroDivisionError:
    print("Error: no se puede dividir por cero")
except Exception as e: # Capturamos cualquier excepción no especificada
    print(f"Error inesperado: {e}")