""""""
# 1- Crea un programa que lea por teclado una cadena y un carácter e inserte el carácter entre cada letra de la cadena

# Usar la función .join
cadena = input("Inserta una palabra: ")
caracter = input("Inserta un carácter: ")

# cadena = list(cadena)
print(cadena)
resultado = caracter.join(cadena)
print(resultado)


# 2- Programa que lea por techado una cadena y carácter y reemplace todos los caracteres de la cadena por el caracter.
cadena2 = input("Introduce una palabra: ")
char = input("Introduce un carácter: ")
resultado2 = char*len(cadena2)
print(resultado2)

# 3- Lee dos cadenas e indica si la segunda cadena es subcadena de la primera.
# Además muestra la primera en orden alfabético
cad3 = input("Introduce una palabra: ")
cad4 = input("Introduce otra palabra: ")
print("¿Es la segunda palabra un substring de la primera? ", cad4 in cad3)
print("La primera palabra el orden alfabético es: ", sorted([cad3, cad4])[0])


# 4- Dada una palabra indica si es palíndromo
palin = input("Introduce una palabra para saber si es palíndromo")
if palin.lower() == palin[::-1].lower():
    print(f"{palin} es palíndromo.")
else:
    print(f"{palin} NO es palíndromo.")