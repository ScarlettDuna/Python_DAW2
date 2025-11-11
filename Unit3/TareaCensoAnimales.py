import numpy as np
# Leemos el archivo iris.csv, lo cargamos en una matriz y descargamos la primera fila y decimos que el separador es la ,
censo = np.genfromtxt('./censo_animales.csv', delimiter=';', skip_header=1, encoding='utf-8')
print("Matriz a partir de archivos de datos. \n", censo)