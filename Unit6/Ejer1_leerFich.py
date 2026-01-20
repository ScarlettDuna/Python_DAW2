#Lectura de ficheros
f = open("files/temps.dat")
# read() carga todo el archivo en memoria RAM a la vez
contenido = f.read()
print(contenido)
f.close() # Imprescindible cerrarlo después de open()

print("\n**** Opción 2 con lista *****")
f = open("files/temps.dat")
# Leemos todas las líneas y las guardamos en una lista
lineas = f.readlines()
for linea in lineas:
    print(linea.strip()) # strip() elimina el salto de linea innecesario
f.close()
print("\n**** Opción 3: línea a línea *****")
f = open("files/temps.dat")
for line in f:
    print(line.strip())
f.close()
