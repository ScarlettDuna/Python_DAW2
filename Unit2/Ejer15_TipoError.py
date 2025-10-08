# Para obtener información de un error
cad = "Hola"
try:
    i = int(cad)
except ValueError as Error:
    print(type(Error))
    print(Error.args)
    print(Error)