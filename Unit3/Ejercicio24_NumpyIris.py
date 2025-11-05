import numpy as np
# Leemos el archivo iris.csv, lo cargamos en una matriz y descargamos la primera fila y decimos que el separador es la ,
iris = np.loadtxt('./iris.csv', skiprows=1, delimiter=',')
print("Matriz a partir de archivos de datos. \n", iris.shape)
# 1. Selecciona 5 filas y calcula la media
iris5filas = iris[:5, :]
print(iris5filas)
print("Media de las 5 filas: ", np.mean(iris5filas, axis=0))
# 2. Usando "axis de mean" calcula la media de las columnas
print("Media del documento: ", (np.mean(iris, axis=0)))
# 3. Encuentra el valor mínimo de cada característica
print("El valor mínimo de cada característica: ", np.min(iris, axis=0))
# 4. Devuelve todas las filas con largo de pétalo (columna 2) mayor que 4
print("Filas cuya longitud de pétalo es mayor que 4: \n", iris[iris[:,2]>4])
# 5. Filas de 50 a 99, pero solo las columnas largo y ancho del pétalo (cols 2 y 3)
irisFilas50a99 = iris[50:100, 2:4]
# print(irisFilas50a99)
# 6. Normalizar para que los valores estén en el rango de 0 a 1
irisNormalizado = (iris - iris.min())/(iris.max()-iris.min())
# print(irisNormalizado)
# 7. Guarda las 4 primeras columns en una variable llamada X
x = iris[:, :4]
# print(x)
# 8. Guarda la última columna en una variable llamada Y
y = iris [:, 4:5]
# print(y)