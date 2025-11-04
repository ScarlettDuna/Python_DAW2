import math
print("**Módulo math")
print("Factorial de 5: ", math.factorial(5))

print("2 al cubo: ", math.pow(2,3))
print("Raíz cuadrada de 7: ", math.sqrt(7))
print("Coseno de 1: ", math.cos(1))
print("Pi: ", math.pi)
print("Logaritmo en base e de 10: ", math.log(10))

# Módulo para fracciones
from fractions import Fraction
print("\n *Fracciones*")
a = Fraction(2, 3)
print("Fraction(2/3) ", a)
b = Fraction(1.5)
print("Fraction(1.5) ", b)
c = a + b
print("Suma de dos fracciones: ", c)

# Módulo para estadística
import statistics
print("\n *Estadística*")
print("Media aritmética de (1+4+5+2+6): ", statistics.mean([1, 4, 5, 2, 6]))
print("Mediana de (1+4+5+2+6): ", statistics.median([1, 4, 5, 2, 6]))


# Módulo random
import random
print("\n *Random*")
print("Número aleatorio en de 10 a 100: ", random.randint(10, 100))

print(random.choice(["hola", "que", "tal", "estás"]))
frutas = ["manzanas", "plátanos", "naranjas"]
print("¿Qué como hoy? ", random.choice(frutas))
random.shuffle(frutas)
print("Lista de frutas mezclada: ", frutas)

lista = [1, 3, 5, 2, 7, 4, 9]
print(lista)
numeros = random.sample(lista, 3)
print(numeros)