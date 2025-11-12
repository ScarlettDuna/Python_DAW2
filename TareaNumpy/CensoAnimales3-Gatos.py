import numpy as np
import matplotlib.pyplot as plt

censo = np.genfromtxt(
    './censo_animales.csv',
    delimiter=';',
    names=True,              # usa la primera fila como nombres de columna
    dtype=None,              # infiere el tipo de cada columna (texto/número)
    encoding='utf-8-sig',        # importante por los acentos
    usecols=(0, 1, 2, 3)
)

distritos = np.unique(censo['DISTRITO'])
mitad = len(distritos) // 2
grupo1 = distritos[:mitad]
grupo2 = distritos[mitad:]

# --- Primera gráfica --- Gatos

colores1 = plt.colormaps['nipy_spectral'](np.linspace(0, 1, len(grupo1))) #Genera colores

plt.figure(figsize=(13, 6))
plt.subplots_adjust(right=0.8)

for d, color in zip(grupo1, colores1):
    datos = censo[censo['DISTRITO'] == d]
    plt.plot(datos['ANO'], datos['ESPECIE_FELINA'], label=d, color=color)

plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.xlabel('Año')
plt.ylabel('Número de gatos')
plt.title('Evolución por distrito - Censo de gatos')
plt.savefig('grafica_gatos1.png')

# --- Segunda gráfica --- Gatos

colores2 = plt.colormaps['nipy_spectral'](np.linspace(0, 1, len(grupo1)))

plt.figure(figsize=(13, 6))
plt.subplots_adjust(right=0.8)
for d, color in zip(grupo2, colores2):
    datos = censo[censo['DISTRITO'] == d]
    plt.plot(datos['ANO'], datos['ESPECIE_FELINA'], label=d, color=color)

plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.xlabel('Año')
plt.ylabel('Número de gatos')
plt.title('Evolución por distrito - Censo de gatos')
plt.savefig('grafica_gatos2.png')
