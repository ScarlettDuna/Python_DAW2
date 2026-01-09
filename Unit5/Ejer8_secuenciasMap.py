# Escribe una función llamada cuadrado que dado un número lo devuelva al cuadrado
def cuadrado(num):
    return num * num

# Lista de números
numeros = [1,2,3,4,5]
# Aplica la función a todos los números de una lista y devuelve un map
resultado = map(cuadrado, numeros)
print(list(resultado))
