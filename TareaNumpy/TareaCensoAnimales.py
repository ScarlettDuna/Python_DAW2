import numpy as np

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
    print(f"{d}:")
    print(matriz)

