# invierte las horas de un reloj de pared
# Si el reloj marca las 03:15 serían las 08:45

# pedir hora y minutos
hora = int(input("Introduce la hora (número del 1 al 12): "))
minutos = int(input("Introduce los minutos (número del 0 al 59): "))
hora_inversa = 0
minutos_inversos = 0
if 1 > hora < 12 or 0 > minutos < 59:
    print("Números no válidos")
else:
    match hora:
        case 1:
            hora_inversa = 11
        case 2:
            hora_inversa = 10
        case 3:
            hora_inversa = 9
        case 4:
            hora_inversa = 8
        case 5:
            hora_inversa = 7
        case _:
            print("Error")
