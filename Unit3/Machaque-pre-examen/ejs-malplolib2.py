import math

import numpy as np
import matplotlib.pyplot as plt

# [largo_sépalo, ancho_sépalo, largo_pétalo, ancho_pétalo, clase]
flores = np.array([
    [5.1, 3.5, 1.4, 0.2, 0],
    [4.9, 3.0, 1.4, 0.2, 0],
    [6.2, 3.4, 5.4, 2.3, 2],
    [5.9, 3.0, 4.2, 1.5, 1],
    [6.0, 2.2, 4.0, 1.0, 1],
    [6.7, 3.1, 5.6, 2.4, 2],
    [5.8, 2.7, 4.1, 1.0, 1],
    [5.0, 3.6, 1.4, 0.2, 0],
    [6.5, 3.0, 5.2, 2.0, 2],
    [5.5, 2.4, 3.7, 1.0, 1],
])
# Selecciona
print("Las primera 4 filas \n", flores[:4,:])
print("Las últimas 3 filas \n", flores[-3:, :])
print("Todas las filas donde el largo de pétalo > 4,5: \n", flores[flores[:,2]>4.5])
print("Todas las filas de la clase 1:\n", flores[flores[:,4] == 1])

# Cálculos
print("Media de cada columna: \n", np.mean(flores, axis=0))
print("Mínimo de cada columna: \n", np.min(flores, axis=0))
print("Máximo de cada columna: \n ", np.max(flores, axis=0))
print("Media del largo del sepalo:\n", np.mean(flores[:,0]))
print("Desviación típica del largo del pétalo: \n", np.std(flores[:,2]))
# norm = (a - a.min()) / (a.max() - a.min())
flores_norm = (flores - flores.min(axis=0)) / (flores.max(axis=0) - flores.min(axis=0))
print("Normalización:\n", flores_norm)

# Operaciones avanzadas
flores_col2y3 = flores[:,1:3]
print(flores_col2y3)
# Calcula la distancia euclídea entre cada flor y la primera flor
# d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
"""
Las primeras 4 columnas son números que importan para distancia:
flores[:, :4]

La primera flor es:
flores[0, :4]
"""
distancias = np.sqrt(np.sum((flores[:, :4] - flores[0, :4])**2, axis=1))
print("Distancias a la primera flor:\n", distancias)

# Ordena el dataset por largo de pétalo
ordenado_por_petalo = flores[np.argsort(flores[:, 2])]
print(ordenado_por_petalo)

# Gráfico de dispersión
plt.subplot(2,2,1)
plt.scatter(flores[:,0][flores[:,4]==0], flores[:,1][flores[:,4]==0], c='blue')
plt.scatter(flores[:,0][flores[:,4]==1], flores[:,1][flores[:,4]==1], c='red')
plt.scatter(flores[:,0][flores[:,4]==2], flores[:,1][flores[:,4]==2], c='green')
plt.xlabel('largo de sépalo')
plt.ylabel('ancho de sépalo')

# Segundo scatter
plt.subplot(2,2,2)
plt.scatter(flores[:,2][flores[:,4]==0], flores[:,3][flores[:,4]==0], c='blue', s=flores[:,0][flores[:,4]==0])
plt.scatter(flores[:,2][flores[:,4]==1], flores[:,3][flores[:,4]==1], c='red', s=flores[:,0][flores[:,4]==1])
plt.scatter(flores[:,2][flores[:,4]==2], flores[:,3][flores[:,4]==2], c='green', s=flores[:,0][flores[:,4]==2])
plt.xlabel('largo de pétalo')
plt.ylabel('ancho de pétalo')

sepalos = flores[:, 0]
media_movil = np.convolve(sepalos, np.ones(3)/3, mode='valid')
plt.subplot(2,2,3)
plt.plot(sepalos, label="Largo del sépalo")
plt.plot(media_movil, label="Media móvil (ventana 3)", linewidth=3)
plt.legend()

plt.subplot(2,2,4)
plt.hist(flores[:,2], color='magenta')

plt.tight_layout()
plt.savefig('scatter.png')

