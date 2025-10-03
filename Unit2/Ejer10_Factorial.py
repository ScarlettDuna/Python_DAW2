# Aplicación que pide un número y calcula el factorial
num = int(input("Introduce un número para saber su factorial"))
factorial = 1
for i in range(2, num + 1):
        factorial *= i

print(f"El factorial de {num} es: {factorial}")