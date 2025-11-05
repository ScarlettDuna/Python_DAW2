import matplotlib.pyplot as plt
import numpy as np

# plots sencillos: eje x de 1-4 y eje y de 1-16
"""
plt.plot([1,2,3,4], [1,4,9,16])
plt.show()"""

# Con 2 líneas
"""
plt.plot([1,2,3,4], [1,4,9,16])
plt.plot([1,2,3,4], [5,1,2,17])
plt.show()"""

# Puntos individuales
"""
plt.scatter([1,2,3,4], [1,4,9,16])
plt.show()"""

#Mezclamos numpy con matplotlib
t = np.arange(0, 5, 0.2)
print(t)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()