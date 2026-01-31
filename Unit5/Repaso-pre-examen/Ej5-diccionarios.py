# Contar frecuencia de palabras en una frase
dic_palabras = {}
parrafo = "Persepolis is the story of Satrapi's unforgettable childhood and coming of age within a large and loving family in Tehran during the Islamic Revolution; of the contradictions between private life and public life in a country plagued by political upheaval; of her high school years in Vienna facing the trials of adolescence far from her family."
lista_parrafo = parrafo.lower().split()
for palabra in lista_parrafo:
    palabra_limpia = palabra.strip(';,.')
    if palabra_limpia not in dic_palabras:
        dic_palabras[palabra_limpia] = 1
    else:
        dic_palabras[palabra_limpia] += 1
print(dic_palabras)
# Traducir una palabra a código morse usando un diccionario dado
morse = {
    'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',   'e': '.',
    'f': '..-.',  'g': '--.',   'h': '....',  'i': '..',    'j': '.---',
    'k': '-.-',   'l': '.-..',  'm': '--',    'n': '-.',    'o': '---',
    'p': '.--.',  'q': '--.-',  'r': '.-.',   's': '...',   't': '-',
    'u': '..-',   'v': '...-',  'w': '.--',   'x': '-..-',  'y': '-.--',
    'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}
parrafo_morse = []
for letra in parrafo.lower():
    if letra in morse:
        parrafo_morse.append(morse[letra])
print(''.join(parrafo_morse))
# Diccionario de personas -> lista de gustos
# Implementar la lógica completa (alta - evitar duplicados)