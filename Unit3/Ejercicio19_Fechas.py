from datetime import datetime
# Mostrar la fecha y la hora actual
ahora = datetime.now()
print("Hora actual ", ahora)


# formatear la fecha en distintos estilos
print("Formato corto: ", ahora.strftime("%d/%m/%Y"))
print("Formato largo: ", ahora.strftime("%A, %d de %B de %Y"))

# Calcular la ead a partir de la fecha de nacimiento
nacimiento = datetime(2005, 11, 21)
hoy = datetime.today()
edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
print("Edad: ", edad)

# Sumar o restar días a una fecha
from datetime import timedelta
fecha_futura = ahora + timedelta(days=30)
print("Me tienes que pagar el: ", fecha_futura)

# Mostrar información del objeto time
from datetime import time
hora_clase = time(8, 30, 0)
print("hora clase: ", hora_clase) # o hora_clase.hour / hora_clase.minute

# Calcular el tiempo de ejecución de un bloque de código
import time
inicio = time.time()
for i in range(10000000):
    pass #no hace nada
fin = time.time()
print("Tiempo de ejecución: ", fin - inicio, " segundos")

import calendar
print(calendar.month(2025, 10))

# Calcular si 2025 es bisiesto
print("Es bisiesto: ", calendar.isleap(2025))

# Cuantos bisiestos hay entre dos fechas
print("Entre 2000 y 2025: ", calendar.leapdays(2000, 2025))