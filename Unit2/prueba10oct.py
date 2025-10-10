distancia = int(input("Introduce km recorridos (0 para terminar): "))
total = 0
lastDay = 0
try:
    while distancia > 0:
        if lastDay == 0:
            lastDay = (distancia * 2)
            total += lastDay
        else:
            lastDay = ((lastDay / 2) + distancia) * 2
            total += lastDay
        distancia = int(input("Introduce km recorridos (0 para terminar): "))
    print(f"La distancia total recorrida (ida y vuelta) es {total}km")
except ValueError:
    print("Tienes que introducir números positivos y '0' para terminar")

