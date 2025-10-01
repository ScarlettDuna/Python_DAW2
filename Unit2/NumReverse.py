# Pide un número de 5 cifras usando solo operaciones sencillas
# pinta el número al revés
num_orig = int(input("Introduce un número de cinco cifras"))
num_invert = ""
for i in range(5) :
    resto = num_orig % 10
    num_invert += str(resto)
    num_orig = num_orig // 10

print(num_invert)