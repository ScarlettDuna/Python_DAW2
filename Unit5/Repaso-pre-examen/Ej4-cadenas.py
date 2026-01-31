# Leer una cadena y:
from itertools import repeat

mi_cadena = input("Introduce una palabra o frase.")
# Contar vocales
vocales = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']
mi_cadena_minusculas = mi_cadena.lower()
contador = 0
for letra in mi_cadena_minusculas:
    if letra in vocales: contador += 1
print(f"La cadena '{mi_cadena}' tiene {contador} vocal{'' if contador == 1 else 'es'}.")
# devolverla invertida
cadena_invertida = mi_cadena[::-1]
print(f"La cadena '{mi_cadena}' invertida es: '{cadena_invertida}'.")
# comprobar si es palíndromo
esPalindromo = mi_cadena_minusculas == cadena_invertida.lower()
print(f"La cadena '{mi_cadena}' es palíndromo: '{'Sí' if esPalindromo else 'No'}'.")
# Reemplazar todos los dígitos de una cadena por X
print(f"La cadena {mi_cadena} si la sustituimos por 'X' {''.join('X' for x in mi_cadena)}")
# En caso de querer sustituir solo los dígitos  -> ''.join('X' if c.isdigit() else c for c in mi_cadena)
# Comprobar si una cadena es subcadena de otra y devolver la menos alfabéticamente
subcadena = input("Introduce un texto para saber si es subcadena de la otra.")
if subcadena in mi_cadena:
    if subcadena < mi_cadena: print(f'{subcadena} es subcadena de {mi_cadena} y va antes alfabéticamente')
    else: print(f'{subcadena} es subcadena de {mi_cadena} pero va después alfabéticamente')
else: print(f'{subcadena} no es subcadena de {mi_cadena}')