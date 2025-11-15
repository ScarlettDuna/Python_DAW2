# Crea un módulo operaciones.py - Impórtalo desde otro archivo y úsalo
import operaciones

print(operaciones.suma(2,4))
print(operaciones.resta(2,4))
print(operaciones.multiplicacion(2,4))

# Módulo OS
import os
# Crea una carpeta
path = os.getcwd()
os.mkdir(path+"/Carpeta_prueba")

# Comprueba si existe
print("Existe la carpeta de prueba:", os.path.exists(path+"/Carpeta_prueba"))
# Listala
print(os.listdir(path))
# Crea un archivo dentro
with open('myfile.txt', 'w') as fp:
    pass

os.rmdir(path+"/Carpeta_prueba")
# Módulo shutil
import shutil
# Copia un archivo, copia un árbol, verifica resultados.
shutil.copy('operaciones.py', 'operaciones_copy.py')
shutil.copytree(path, path+"_copy")

# Módulo datetime
from datetime import datetime
# Calcula la edad
hoy = datetime.today()
nacimiento = datetime(1991, 4, 20)
edad = hoy.year - nacimiento.year
print("Edad: ", edad)
# Suma 100 días
from datetime import timedelta
nueva_fecha = hoy + timedelta(days=100)

# Dime si un año es bisiesto
import calendar
es_bisiesto = calendar.isleap(2021)
es_bisiesto2 = calendar.isleap(2004)

# Mide ejecución de un bloque
import time
def mide_ejecucion():
    inicio = time.time()
    for i in range(1000):
        pass
    fin = time.time()
    return fin - inicio