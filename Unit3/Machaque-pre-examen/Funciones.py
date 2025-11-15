# Crea una función que acepte cualquier número de números y devuelva:
def calculadora(*nums):
    if nums:
        suma = sum(nums)
        maximo = max(nums)
        media = suma / len(nums)
        return suma, media, maximo
    return "Introduce un array de números"

print(calculadora(3,9,2,7))
# Función con kwargs obligatorios
def crear_usuario(**kwargs):
    obligatorios = ["nombre", "edad"]

    for key in obligatorios:
        if key not in kwargs:
            raise TypeError(f"Falta el argumento obligatorio '{key}'")

    return "Usuario creado"

# Reescribe una función usando lambda def doble(x): return x*2
doble = lambda x: x*2

# Crea un decorador que mida el tiempo de ejecución
import time
def decorador(funcion):
    def wrap(*args, **kwargs):
        inicio = time.time()
        r = funcion(*args, **kwargs)
        fin = time.time()
        print("El tiempo de ejecución de la función es: ", fin - inicio)
        return r
    return wrap
# Crea un generador que devuelva números pares hasta n
def gen_pares(n):
    num = 0
    while num <= n:
        yield num
        num += 2
    """for i in range(0, n, 2):
            yield i"""
for n in gen_pares(10):
    print(n)

# Función que recibe listas o diccionarios y los desempaqueta
def desempaquetar(*lista):
    for item in lista:
        if isinstance(item, dict):
            for valor in item.values():
                yield valor
        elif isinstance(item, (list, tuple)):
            for valor in item:
                yield valor
        else:
            yield item

# Función que devuelva varias cosas. Dada una lista, devuelve: el listado ordenado, mínimo, y el índice del máximo
def multiusos(*lista_numeros):
    ordenados = sorted(lista_numeros)
    idx_max = 0
    for n in range(0, len(lista_numeros)):
        if lista_numeros[n] > lista_numeros[idx_max]:
            idx_max = n
    return ordenados, lista_numeros[idx_max], idx_max
