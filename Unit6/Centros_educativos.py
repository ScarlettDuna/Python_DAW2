import pandas as pd
import matplotlib.pyplot as plt

archivo_centros = pd.read_csv('files/centros-educativos.csv', sep=';', encoding='latin-1')

# print(archivo_centros.head())

conteo_distritos = archivo_centros['DISTRITO'].value_counts()

# Creamos un diccionario de los distritos con el número de centros por distrito
dic_distritos = conteo_distritos.to_dict()
print(dic_distritos)

# Creamos un diccionario de los distritos con el número de centros por distrito
dic_tipos = archivo_centros['TIPO'].value_counts().to_dict()
print(dic_tipos)

# El distrito que más centros tiene
masCentros = conteo_distritos.idxmax()

# Creación informe
with open("files/informe_Arantxa.txt", "w", encoding="utf-8") as f:
    f.write("INFORME DE CENTROS EDUCATIVOS\n")
    f.write(f"\nTotal de centros: {len(archivo_centros)}\n")
    f.write(f"\nCentros por tipo: \n")
    # Para quedarse solo con la última parte key.split('/')[-1]
    for [key, value] in dic_tipos.items():
        f.write(f"{key.split('/')[-1]}: {value}\n")
    f.write(f"\nCentros por distrito:")
    for [key, value] in dic_distritos.items():
        f.write(f"{key}: {value}\n")
    f.write("\nDISTRITO CON MÁS CENTROS:\n")
    f.write(f"\nEl distrito con mayor oferta educativa es: {masCentros}.\n")

plt.bar(dic_distritos.keys(), dic_distritos.values())
plt.xticks(rotation=45, ha='right')
plt.xlabel('Distritos')
plt.ylabel('Cantidad')
plt.title('Distribución de Centros por Distrito by Arantxa R.')
plt.tight_layout()
plt.savefig('grafica_distritos.png')
plt.show()
