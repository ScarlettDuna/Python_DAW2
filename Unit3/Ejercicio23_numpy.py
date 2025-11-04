import numpy as np
# A.
matrizA = np.ones((2, 3))
matrizB = np.arange(1, 7).reshape((2, 3))
matrizAmasB = matrizA + matrizB
print(matrizAmasB)

# B.
matrizC = np.array([[1], [3], [5]])
matrizD = np.array([2, 4, 6])
matrizCporD = np.matmul(matrizC, matrizD)
print(matrizCporD)

# C. Una matriz 4 x 4 cuyos valores vayan de 1 a 16, pero dónde los números pares han sido sustituidos por -1

