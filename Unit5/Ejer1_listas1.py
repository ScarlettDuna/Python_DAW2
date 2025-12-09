# Definir una lista
lista = [1, 2, 3, 4, 5]
print("Recorriendo la lista")
for num in lista:
    print(num, end=' ')

print("Está el 2 en la lista", 2 in lista)
print("El 8 NO está en la lista", 8 not in lista)

# concatenar
nuevalista = lista+[6, 7, 8, 9]
print("Nueva lista: ", nuevalista)

# Repetición
print("lista*2: ", lista*2)

# Acceder
print("Elemento en posición 4: ", lista[3])

# Slice (rebanada)
print("Subsecuencia de lista ", lista[2:4])

# Otro slice
print("Subsecuencia de lista con salto ", nuevalista[1:4:2]) # Del 1 al 4 de 2 en 2

# num elementos
print("Longitud: ", len(lista))

# máximo y mínimo
print("Máximo: ", max(lista))
print("Mínimo: ", min(lista))

# Como es mutable puedo cambiar un elemento
lista[2] = 99
print("lista: ", lista)

lista[2:4] = [80, 90, 100]
print("Lista cambiada2: ", lista)

del nuevalista [5:]
print(nuevalista)