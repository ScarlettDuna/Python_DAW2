import numpy as np
print("Versión: ", np.__version__)

# Un array es una estructura similar a una lista, pero optimizada para cálculos numéricos
a = np.array([1, 2, 3])
print("Mi primer array en numpy: ", a)

print("\n *Crear Arrays*")
print("Array de enteros: ", np.array([10, 20, 30]))
print("Array de ceros: ", np.zeros(5))
print("Array de unos que tenga 2 files y 3 columnas: ")
print(np.ones((2, 3)))
print("Array desde 0 hasta 10 contando de 2 en 2")
print(np.arange(0, 10, 2))
print("Array con valores aleatorios en 3 filas y 2 columnas")
print(np.random.rand(3, 2))

# Matriz 2 x 2
mat1 = np.array([[1, 2], [3, 4]])
print(mat1)
# Matriz de unos de 2 x 2
mat2 = np.ones((2, 2))
print(mat2)

# Comprobar dimensión de la matriz
print("Dimensión de la matriz 2: ", mat2.shape, "\n")

#Sumar matrices
matSuma = mat2 + mat1
print("Suma de matrices: ", matSuma)

# Multiplicar matriz por un valor
matMulti = mat1 * 2
print("MatMult\n", matMulti)

# Multiplicación de matrices
print("Multiplicación matricial opción 1: \n", np.matmul(mat1, mat2))
print("Multiplicación de matrices opción 2: \n", mat1 @ mat2, "\n")

#Inversa de la matriz, la inversa de una matriz es la matriz que al multiplicar por la matriz original da la matriz identidad
# La matriz identidad tiene unos en la diagonal ceros en el resto
print("Dada la matriz 1: \n", mat1)
print("La inversa es: \n", np.linalg.inv(mat1))
# Comprobación
print("Comprobación: ", np.matmul(mat1, np.linalg.inv(mat1)))

# Crear una matriz con valores del 1 al 9 de forma rápida
mat3 = np.arange(1, 10).reshape((3, 3))
print("Matriz del 1 al 9: \n", mat3)
print("Matriz del 1 al 9 traspuesta: \n", mat3.T)

# Seleccionar celdas
print("fila2, columna2", mat3[1,1])
print("Toda la fila2: ", mat3[1,:])
print("Toda la columna3: ", mat3[:,2])
print("Dimensiones mat3: ", mat3.shape)

# Filtrado
print("De la matriz quedate con números > 5: ", mat3[mat3>5])
print("Media de la matriz mat3: ", np.mean(mat3))
print("Media de filas: ", np.mean(mat3, axis=1))
print("Media de columnas: ", np.mean(mat3, axis=0))