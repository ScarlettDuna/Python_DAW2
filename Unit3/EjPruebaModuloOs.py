import os
import shutil
from datetime import datetime
from sys import exception

# Crea un programa que realice las tareas de backup de una carpeta de nuestro sistema. (C:origenXXX)
# Crear un directorio de origen y algunos archivos de prueba dentro de él.
origen = "D:\\origenARG"
try:
    print(os.access(origen, os.R_OK))
    # Crear un directorio de destino donde se guardarán los respaldos (C: destinoXXX)
    hoy = datetime.today()
    destino = f"D:\\destinoARG{hoy.strftime("%d-%m-%Y")}Ejercicio"
    os.makedirs(destino, exist_ok=True)
    # Copiar un archivo específico del origen al destino usando shutil.copy()
    shutil.copy(origen+"\\Archivo2.txt", destino)
    # Copiar tdo el contenido de un directorio (incluyendo subdirectorios y archivos) del origen al destino usando shutil.copytree()
    shutil.copytree(origen, destino, dirs_exist_ok=True)
    # Verificar que los archivos y directorios se copiaron correctamente (imprimiendo por consola el contenido del directorio destino)
    os.listdir(destino)
except exception as e:
    print(e)