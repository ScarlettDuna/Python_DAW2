# Métodos de inserción en listas
lista = [1,2,3]
lista.append(4)
print(lista)
lista2 = [5,6]
lista.extend(lista2)
print("lista", lista)
lista.insert(1, 100)
print("lista", lista)
print("lista.pop()", lista.pop())
print("lista.pop(1)", lista.pop(1))
lista.remove(3)
print("lista después de remove: ", lista)

#ordenar la lista
lista.reverse()
print("lista reversed: ", lista)
lista.sort()
print("lista sorted: ", lista)
# o lista.sort(reverse=True)
lista3 = [1,2,3,4,5]

print("¿Cuántos 5 hay? ", lista3.count(5))
print("¿En qué posición está el 5? ", lista.index(5))
print("¿En qué posición está el 5? ", lista.index(5, 1, 4)) #ValueError
