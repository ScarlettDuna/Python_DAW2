import numpy as np
# Leemos el archivo iris.csv, lo cargamos en una matriz y descargamos la primera fila y decimos que el separador es la ,
iris = np.loadtxt('./iris.csv', skiprows=1, delimiter=',')
print("Matriz a partir de archivos de datos. \n", iris.shape)

# 1. Selecciona 5 filas y calcula la media

# 2. Usando "axis de mean" calcula la media de las columnas

# 3. Encuentra el valor mínimo de cada característica

# 4. Devuelve todas las filas con largo de pétalo (columna 2) mayor que 4

# 5. Filas de 50 a 99, pero solo las columnas largo y ancho del pétalo (cols 2 y 3)


# 6. Normalizar para que los valores estén en el rango de 0 a 1


# 7. Guarda las 4 primeras columns en una variable llamada X


# 8. Guarda la última columna en una variable llamada Y