# Ejemplo de finally
archivo = None

try:
    #trozo de código que puede fallar
    archivo = open("mi_archivo.txt",  "r")
    contenido = archivo.read()
    print("Contenido del archivo: ", contenido)
except FileNotFoundError: # Tipo de error
    print("No encuentro el archivo")
finally: # Código que se ejecuta tanto si va bien como si falla
    if archivo: # Nos aseguramos de que está abierto antes de cerrarlo
        archivo.close()
        print("El archivo se ha cerrado")
