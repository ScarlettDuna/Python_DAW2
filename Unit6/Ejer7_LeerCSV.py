import csv
with open("files/alumnos.csv", "r", encoding="utf-8") as f:
    lector = csv.reader(f)
    for fila in lector:
        # Cada fila es una lista
        print(f"Nombre {fila[0]}, Edad: {fila[1]}, Ciudad: {fila[2]}")

# Opción 2 - pandas integra en la misma línea el with y el close
import pandas as pd
df = pd.read_csv("files/alumnos.csv")
print("Leemos las primeras 5 líneas")
print(df.head())
# Calcular la media de la edad
print("La media de la edad: ", df['edad'].mean())