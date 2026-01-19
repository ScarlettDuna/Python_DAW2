frase = "manzana pera manzana naranja pera manzana".split(' ')
print(frase)
frecuencia = {}
for fruta in frase:
    if fruta in frecuencia:
        frecuencia[fruta] += 1
    else:
        frecuencia[fruta] = 1
print(frecuencia)
"""
for fruta in frase:
    # Si fruta no existe, devuelve 0 y le suma 1. Si existe, suma 1 al valor actual.
    frecuencia[fruta] = frecuencia.get(fruta, 0) + 1"""