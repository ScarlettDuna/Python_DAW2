# Con el módulo os accedemos a funcionalidades del sistema
import os
print("Directorio actual: ", os.getcwd())
path = os.getcwd()
print("Path absoluto: ", os.path.abspath(path))
print("Directorio base: ", os.path.basename(path))
print("Saber si un directorio existe", os.path.exists(path))
print("Último acceso a un directorio: ", os.path.getatime(path))
print("Tamaño del directorio: ", os.path.getsize(path))
print("Saber si es una ruta absoluta: ", os.path.isabs(path))
print("Saber si una ruta es un archivo: ", os.path.isfile(path))
print("Saber si una ruta es un directorio: ", os.path.isdir(path))
print(os.system("dir"))