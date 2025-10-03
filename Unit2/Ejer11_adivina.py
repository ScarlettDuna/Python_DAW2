# Programa que permite adivinar un número
# Se pide un número por pantalla
# después de van pidiendo números y respondiendo si es mayor o menor
from random import randint

print("Vamos a jugar a \'Adivina el número\'")
# num_aleatorio = int(input("Introduce el número a adivinar"))
num_aleatorio = randint(1,50)
guess = int(input("Introduce un número "))
while guess != num_aleatorio:
    if guess < num_aleatorio:
        print("Es mayor")
    elif guess > num_aleatorio:
        print("Es menor")
    guess = int(input("Introduce otro número "))

if guess == num_aleatorio:
    print(f"¡Has acertado! Era el número {num_aleatorio}")