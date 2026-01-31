# Dada una lista de números
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
# Usa map para elevar al cuadrado
numeros_cuadrado = list(map(lambda x: x**2, lista_numeros))
print(numeros_cuadrado)
# Usa filter para quedarte con los mayores de 10
mayores_diez = list(filter(lambda  x: x>10, numeros_cuadrado))
print(mayores_diez)
# Usa reduce para calcular la suma
from functools import reduce
suma = reduce(lambda a,b: a+b, mayores_diez, 0)
print(suma)