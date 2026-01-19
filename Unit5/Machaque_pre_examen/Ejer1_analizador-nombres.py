nombres_alumnos = ["Ana", "Juan", "ana", "Pedro", "JUAN"]
nombres_minusculas = set([name.lower() for name in nombres_alumnos])

print(nombres_minusculas)
dic_nombre_len = {name: len(name) for name in nombres_minusculas}
print(dic_nombre_len)