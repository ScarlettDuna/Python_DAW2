# Factorial
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n//10)
print(suma_digitos(12345))

def potencia(a, b):
    if b == 0:
        return 1
    else:
        return a * potencia(a, b-1)
print(potencia(2, 5))

def reverso(array):
    if len(array) == 1:
        return array
    else:
        return array[-1:] + reverso(array[:-1])
print(reverso([1, 2, 3]))

def contar(array):
    if not array:
        return 0
    else:
        return 1 + contar(array[:-1])
print(contar([1, 2, 3, 4, 5]))

def buscar(array, x):
    if array[0] == x:
        return True
    else:
        if not array[1:]:
            return False
        else:
            return buscar(array[1:], x)
print("Buscar \nTrue expected: ", buscar([1, 2, 3, 4, 5], 3))
print("False expected: ", buscar([1, 2, 3, 4, 5], 6))

def maximo(array):
    if len(array) == 1:
        return array[0]
    else:
        resto = maximo(array[1:])
        return array[0] if array[0] > resto else resto
print(maximo([3,9,2,7,10,-7]))

def es_palindromo(palabra):
    if len(palabra) > 1:
        if palabra[0] != palabra[-1]:
            return False
        else:
            return es_palindromo(palabra[1:-1])
    return True
print(es_palindromo('radar'))
print(es_palindromo('amma'))

def contar_ap(array, x):
    if len(array) == 0:
        return 0
    if array[0] == x:
        return 1 + contar_ap(array[1:], x)
    else:
        return contar_ap(array[1:], x)
print(contar_ap( [2,3,2,4,2], 2 ))

def fibonacci(n, dic=None):
    # Inicias el diccionario en la primera llamada
    if dic == None:
        dic = {}
    # Caso base / que rompe las llamadas interminables
    if n in dic:
        return dic[n]
    # Creas los casos del diccionario
    if n == 0:
        dic[n] = 1
    elif n == 1:
        dic[n] = 1
    else:
        dic[n] = fibonacci(n-2, dic) + fibonacci(n-1, dic)
    return dic[n]
print(fibonacci(11))

def torres_Hanoi(n):
    # – Si hay 1 disco → 1 paso.
    if n == 1:
        return 1
    # – Si hay n discos → 2 * pasos(n-1) + 1.
    else:
        return 2 * torres_Hanoi(n-1) + 1
print("Torres de Hanoi\n", torres_Hanoi(3))
print(torres_Hanoi(4))
print(torres_Hanoi(7))

def aplanar_lista(lista):
    if not lista:
        return lista
    else:
        cabeza = lista[0]
        cola = lista[1:]
        if isinstance(cabeza, list):
            return aplanar_lista(cabeza) + aplanar_lista(cola)
        else:
            return [cabeza] + aplanar_lista(cola)
print(aplanar_lista([1, [2, 4, [3], 5]]))

def sumar_lista(lista, ):
    if lista:
        cabeza = lista[0]
        cola = lista[1:]
        if isinstance(cabeza, int) or isinstance(cabeza, float):
            return cabeza + sumar_lista(cola)
        else:
            return sumar_lista(cabeza) + sumar_lista(cola)
    else:
        return 0
print(sumar_lista([1, [2, 4, [3], 5]]))

# Si tienes [1, 2, 3], las permutaciones son:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1].
def permutaciones(array):
    if len(array) <= 1:
        return [array]

    resultado = []

    for i in range(len(array)):
        elem = array[i]
        resto = array[:i] + array[i + 1:]

        subperms = permutaciones(resto)

        for p in subperms:
            resultado.append([elem] + p)

    return resultado
print(permutaciones([1,2,3]))

def contar_hasta(n):
    if n != 1:
        print(n)
        return contar_hasta(n-1)
    else:
        return print(1)
contar_hasta(5)