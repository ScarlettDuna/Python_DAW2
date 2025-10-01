# Programa que pide un número entero e imprime el número de días del mes
num = int(input("Introduce un número del 1 al 12"))

match num:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("Este mes tiene 31 días")
    case 2:
        print("Este mes tiene 28 días, o 29 si el año el bisiesto.")
    case 4 | 6 | 9 | 11:
        print("Este mes tiene 30 días")
    case _:
        print("Número no válido")
