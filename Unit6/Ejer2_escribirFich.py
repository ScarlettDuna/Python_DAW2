# Opción 1
f = open("files/nuevo_archivo.txt", "w", encoding="utf-8")
# Escribir una cadena simple
f.write("Hola, esta es la primera línea")
f.write("\nY esta la segunda")
f.close()

print("Fichero generado correctamente")
f = open("files/nuevo_archivo.txt", "a", encoding="utf-8")
texto_anadido = "Texto añadido con append"
f.write('\n'+texto_anadido)