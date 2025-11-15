import numpy as np
# Crea arrays de 1D, 2D y 3D
un_d = np.array([1,2,3,4])
dos_d = np.array([[1,2,3,4], [5,6,7,8]])
tres_d = np.array([                 # 3 bloques
    [[1,2,3],[4,5,6]],              # 2x3
    [[7,8,9],[10,11,12]],           # 2x3
    [[13,14,15],[16,17,18]]         # 2x3
])

# Opera entre arrays: suma, multiplicación, potencia, broadcasting
dos_por_dos = np.random.rand(2, 2)
dos_por_dos2 = np.arange(1, 5).reshape((2, 2))
print(dos_por_dos * 2)
print(dos_por_dos2 + dos_por_dos)
print(dos_d ** 2) # np.square(dos_d)
# Multiplicación de matrices
print(dos_por_dos @ dos_por_dos2)

# Estadística
print("El valor mínimo: ", np.min(dos_d))
print("La suma de los valores: ", np.sum(tres_d))
print("Mediana ", np.median(tres_d))
print("Media: ", np.mean(un_d))

# Normalización
# norm = (a - a.min()) / (a.max() - a.min())
tres_d_norm = (tres_d - np.min(tres_d)) / (np.max(tres_d) - np.min(tres_d))
print("tres_d normalizada:\n", tres_d_norm)
# Filtrado
print(dos_d[dos_d % 2 == 0])

# Dataset Iris
iris = np.loadtxt('../iris.csv', skiprows=1, delimiter=',')
# Primeras cinco filas
iris_5filas = iris[:5, :]
print(iris_5filas)
# Media global
print("Media global: ", np.mean(iris))
# media por columna
print("Media por columnas: ", np.mean(iris, axis=0))
# Mínimo por columna
print("Mínimo por columna: ", np.min(iris, axis=0))
# Filtrar pétalo largo > 5
print(iris[iris[:,2] > 5])
# Filas 50-99, columas 2 y 3
iris_3 = iris[50:100, 2:4]
print(iris_3)
# Normaliza todo
iris_norm = (iris - np.min(iris)) / (np.max(iris) - np.min(iris))