# 1. qué día de la semana se produce el mayor número de ventas
# 2. qué día de la semana se produce el menor número de ventas
# 3. si las ventas del domingo superan a la media semanal.
dias = ["MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO", "DOMINGO"]
recaudacion = [None, None, None, None, None, None]
try:
    for i in range(6):
        recaudacion[i] = int(input(f"Inserte la recaudación del {dias[i]} "))
except ValueError:
    print("Debes introducir números")

print(recaudacion)
masVentas = 0
menosVentas = 0
total = 0
for i in range(6):
    if recaudacion[i] > recaudacion[masVentas]:
        masVentas = i
    if recaudacion[i] < recaudacion[menosVentas]:
        menosVentas = i
    total += recaudacion[i]
    print(f"Recaudación del {dias[i]}: {recaudacion[i]}")
mediaSemana = total / 6
print("Mejor día: ", dias[masVentas])
print("Peor día: ", dias[menosVentas])
def DomingoSemana(domingo, media):
    if domingo > media:
        print("Sí")
    else:
        print("No")
DomingoSemana(recaudacion[5], mediaSemana)