# El map transforma, el filter selecciona y el reduce se aplica a todos los elementos de una lista
from functools import reduce

def sumar(x,y):
    return x+y

numeros = [1,2,3,4,5,6]

resultado = reduce(sumar, numeros)
print(resultado)
