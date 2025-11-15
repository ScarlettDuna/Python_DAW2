import numpy as np
import matplotlib.pyplot as plt

#  [altura (cm), diámetro tallo (mm), ancho hoja (cm), nº hojas, especie]
plantas = np.array([
    [12.5, 3.1, 5.0, 14, 0],
    [15.3, 2.9, 4.8, 12, 0],
    [32.1, 5.4, 9.6, 22, 2],
    [28.4, 4.9, 8.7, 18, 1],
    [30.0, 4.7, 8.4, 20, 1],
    [35.2, 5.8, 10.1, 24, 2],
    [27.1, 4.5, 8.0, 19, 1],
    [13.0, 3.3, 5.2, 15, 0],
    [33.5, 5.6, 10.0, 23, 2],
    [26.8, 4.3, 7.9, 17, 1],
])
# Selección y filtrado
print("Primeras 5 filas: \n", plantas[:5,:])
print("Las últimas 4 filas:\n", plantas[-4:,:])
print("Las plantas con ancho de hoja > 8,5:\n", plantas[plantas[:,2]>8.5])
print("Plantas de la especie 1:\n", plantas[plantas[:,4] == 1])
print("Las plantas con altura menos que la media de la columna altura:\n", plantas[plantas[:,0]< np.mean(plantas[:,0])])

# Cálculos
print("Media de cada columna:\n", np.mean(plantas, axis=0))
print("Mínimo de cada columna:\n", np.min(plantas, axis=0))
print("Máximo de cada columna:\n", np.max(plantas, axis=0))
print("Desviación típica del número de hojas:\n", np.std(plantas[:,3]))
plantas_norm = (plantas - plantas.min(axis=0)) / (plantas.max(axis=0)-plantas.min(axis=0))
print("Normalización por columnas:\n", plantas_norm)

# Operaciones avanzadas
print("Columnas de altura y ancho de hoja\n", plantas[:, [0, 2]])

#Calcula la distancia euclídea de todas las plantas respecto a la primera (solo usando columnas 0 y 2)
# d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
distancias = np.sqrt(np.sum((plantas[:, [0,2]] - plantas[0, [0,2]])**2, axis=1))
print(distancias)

# Ordena el dataset por número de hojas
plantas_hojas = plantas[np.argsort(plantas[:,3])]
print(plantas_hojas)

# Ordena el dataset por altura en orden descendente
plantas_alt_desc = plantas[np.argsort(-plantas[:,0])]
print(plantas_alt_desc)

# Gráfica scatter a
plt.subplot(3,2,1)
plt.scatter(plantas[:,0][plantas[:,4]==0], plantas[:,2][plantas[:,4]==0], c='y', s=plantas[:,1][plantas[:,4]==0]* 2)
plt.scatter(plantas[:,0][plantas[:,4]==1], plantas[:,2][plantas[:,4]==1], c='g', s=plantas[:,1][plantas[:,4]==1]* 2)
plt.scatter(plantas[:,0][plantas[:,4]==2], plantas[:,2][plantas[:,4]==2], c='b', s=plantas[:,1][plantas[:,4]==2]* 2)
plt.xlabel('altura')
plt.ylabel('ancho de hoja')

# Gráfica scatter b
plt.subplot(3,2,2)
plt.scatter(plantas[:,1][plantas[:,4]==0], plantas[:,3][plantas[:,4]==0], c='y', marker='x')
plt.scatter(plantas[:,1][plantas[:,4]==1], plantas[:,3][plantas[:,4]==1], c='g', marker='x')
plt.scatter(plantas[:,1][plantas[:,4]==2], plantas[:,3][plantas[:,4]==2], c='b', marker='x')
plt.xlabel('diámetro del tallo')
plt.ylabel('nº de hojas')

# Gráfica línea + media móvil c
plt.subplot(3,2,3)
altura = plantas[:, 0]
media_movil = np.convolve(altura, np.ones(3)/3, mode='valid')
plt.plot(plantas[:,0], c='magenta')
offset = 3//2
plt.plot(range(offset, offset + len(media_movil)), media_movil, color='yellow')
plt.xlabel('altura')

# Histograma
plt.subplot(3,2,4)
plt.hist(plantas[:,2], color='orange')
plt.xlabel('Ancho de hoja')

# Heatmap
plt.subplot(3,2,5)
plt.imshow(plantas_norm, cmap='viridis')
plt.colorbar()
plt.title("Heatmap matriz normalizada")

plt.tight_layout()
plt.savefig('plantas.png')