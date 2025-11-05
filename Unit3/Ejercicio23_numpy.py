import numpy as np
# A.
matrizA = np.ones((2, 3))
matrizB = np.arange(1, 7).reshape((2, 3))
matrizAmasB = matrizA + matrizB
print(matrizAmasB)

# B.
matrizC = np.array([[1], [3], [5]])
matrizD = np.array([[2, 4, 6]])
matrizCporD = matrizC @ matrizD
print(matrizCporD)

# C. Una matriz 4 x 4 cuyos valores vayan de 1 a 16, pero dónde los números pares han sido sustituidos por -1
matriz4x4 = np.arange(1, 17).reshape((4, 4))
matriz4x4[matriz4x4 % 2 == 0] = -1
print(matriz4x4)

# D.
matrizCompleja = np.array([[2+0.j, 3+0.j, 4+0.j], [5+0.j, 6+0.j, 7+0.j]], dtype=complex)
print(matrizCompleja)