# Programa que pida un número (minutos) y diga cuantas horas son
minutos = input("Introduce los minutos")

horas = int(minutos) / 60 # Si se utiliza // se queda solo con la parte entera del número por defecto.
min_restantes = int(minutos) % 60

print(str(minutos) + " son " + str(int(horas)) + " horas y " + str(min_restantes) + " minutos.")

# Programa que pida nombre y un número y lo muestre por pantalla
nombre = input("Introduce tu nombre")
num = input("Introduce un número")

print("Nombre elegido " + nombre + " \n Número elegido " + num)