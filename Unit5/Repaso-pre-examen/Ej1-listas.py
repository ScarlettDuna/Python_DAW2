# Lee números hasta que sea negativo
lista_numero = []
numero = int(input("Añade un número positivo a la lista, para salir introduce un negativo"))
while numero > 0:
    lista_numero.append(numero)
    numero = int(input("Añade un número positivo a la lista, para salir introduce un negativo"))
print(lista_numero)

# Dada una lista, devolver otra invertida sin usar reverser()
lista_num_invertida = lista_numero[::-1]
print(lista_num_invertida)

# Comprobar si una lista está ordenada ascendentemente.
def estaOrdenada(miLista):
    if miLista == sorted(miLista):
        return True
    else:
        return False
print(estaOrdenada(lista_numero))