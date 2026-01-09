# List comprehension
# Para transformar elementos se usa la estructura [expresión for elemento in iterable]
numeros = [1,2,3,4,5,6]
cuadrados = [x*x for x in numeros]
print(cuadrados)

# otro ejemplo: obtener pares
pares = [x for x in numeros if x % 2 == 0]
print(pares)

# eleva al cuadrado los numeros pares
pares_cuadrados = [x*x for x in numeros if x % 2 == 0]
print(pares_cuadrados)