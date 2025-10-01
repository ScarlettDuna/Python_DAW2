# Pedir un número por pantalla y mostrar la tabla de multiplicar
num = int(input("Introduce un número para saber su tabla de multiplicar: "))
print(f"Tabla del número {num}")
for i in range(1, 11):
    print(f"{i} x {num} = {i*num}")

