#Hay conversiones explícitas e implícitas
# 1 - Implícito
entero = 5
decimal = 2.5

resultado = entero + decimal # Python convierte el entero a decimal
print(resultado)
print(type(resultado))

# 2 - Explícito (forzada por el programa)
numero_str = "42"
numero_int = int(numero_str)
print(numero_int)

# convertimos de float a entero
pi = 3.14159
entero_pi = int(pi)
print(entero_pi)

# De entero a string
edad = 30
mensaje = "Tienes " + str(edad) + " años."
print(mensaje)