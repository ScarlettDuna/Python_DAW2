distancia = int(input("Introduce la distancia en metros"))
vel_maxima = int(input("Introduce la velocidad en km/h"))
tiempo_rec = int(input("Introduce el tiempo transcurrido en segundos"))

vel_max_ms = (vel_maxima*1000) / 3600

vel_real = distancia / tiempo_rec
if vel_real > vel_max_ms:
    if vel_real < (vel_max_ms * 1.2):
        print("MULTA")
    else:
        print("PUNTOS")
else:
    print("OK")