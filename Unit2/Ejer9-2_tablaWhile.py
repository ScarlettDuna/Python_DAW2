# Pedir un número por pantalla y mostrar la tabla de multiplicar
num = int(input("Introduce un número para saber su tabla de multiplicar: "))
print(f"Tabla del número {num}")
i = 1
while i <= 10:
    print(f"{num} x {i} = {i*num}")
    i += 1
