distancia = 1
total = 0
last_day = 0
while distancia > 0:
    # control de excepciones solo en la entrada de datos
    try:
        distancia = int(input("Introduce km recorridos (0 para terminar): "))
    except ValueError:
        print("Tienes que introducir números positivos y '0' para terminar")
    # para evitar que ejecute el código cuando se introduce 0 rompemos el bucle
    if distancia == 0:
        break
    # Comprobación para que no aumenten más de 30 km, y vuelve al principio del bucle
    elif distancia > 30:
        print("No se puede incrementar más de 30km el entrenamiento entre días.")
        continue
    # Por si acaso meten un dato negativo vuelve el principio del bucle
    elif distancia < 0:
        print("la distancia debe ser un número positivo o 0 para terminar.")
        continue
    if last_day == 0:
        last_day = (distancia * 2)
        total += last_day
    else:
        last_day = ((last_day / 2) + distancia) * 2
        total += last_day

print(f"La distancia total recorrida (ida y vuelta) es {total}km")


