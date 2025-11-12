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
# print("Matriz a partir de archivos de datos. \n", censo)
print(censo.dtype.names)

distritos = np.unique(censo['DISTRITO'])
print(distritos)
anyos = np.unique(censo['ANO'])
print(anyos)

for d in distritos:
    datos = censo[censo['DISTRITO'] == d]
    matriz = np.column_stack((datos['ANO'], datos['ESPECIE_CANINA'], datos['ESPECIE_FELINA']))
    plt.figure(figsize=(10, 6))
    plt.subplots_adjust(right=0.8)
    plt.plot(datos['ANO'], datos['ESPECIE_FELINA'], label="GATOS")
    plt.plot(datos['ANO'], datos['ESPECIE_CANINA'], label="PERROS")
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.xlabel('Año')
    plt.ylabel('Número de perros')
    plt.title(f"Evolución {d}")
    plt.savefig(f"grafica_{d}.png")
    plt.close()

