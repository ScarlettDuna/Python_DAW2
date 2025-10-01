# Recopilación de datos
superficie = int(input("Introduce la superficie en metro cuadrados."))
num_campos = int(input("Introduce la estimación de campos de fútbol"))

# Calculamos el área de los campos de fútbol más pequeño y más grande
campo_grande = 120 * 90
campo_pequeno = 90 * 45

# Comprobación de datos introducidos y control de flujo para saber si es verdadero o falso
if (superficie < 0 or superficie > 100000) or (num_campos < 0 or num_campos > 100000):
    print("Datos no validos")
else:
    if (num_campos * campo_grande >= superficie) and (num_campos * campo_pequeno <= superficie):
        print("Verdadero")
    else:
        print("Falso")

