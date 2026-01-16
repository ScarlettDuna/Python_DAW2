# Diccionario, tipo de datos mutable parecido a json (clave-valor)
dic1 = dict(one=1, two=2, three=3)
print(dic1)
dic2 = {'one':1, 'two':2, 'three':3}
print(dic2)
dic3 = dict(zip(['one', 'two', 'tree'], [1,2,3]))
print(dic3)
dic4 = dict([('two',2), ('three',3), ('one', 1)])
print(dic4)

# más formas de diccionario
dict5 = {}
dict5['one'] = 1
dict5['two'] = 2
dict5['three'] = 3
print(dict5)

# Copiar al diccionario
dict6 = dict5.copy()

# Operaciones básicas
print('len: ', len(dict5))
print(dict5['one'])
del(dict5['one'])
print('dict5 tras borrar: ', dict5)
print('¿Está dos? ', 'two' in dict5)
dict5.clear()
print('dict6 tras clear(): ', dict6)

dict7 = {'four': 4, 'five': 5}
print(dict7)
dict5.update(dict7) # revisar esto
print('dict5 ahora: ', dict5)

print('El cuatro', dict5.get('four'))
print('El acuatro con pop: ', dict5.pop('four'))
print('popitem: ', dict5.popitem())
print('dict5 ahora: ', dict5)
print('Lista de items: ', dict6.items())
print('Lista de claves: ', dict6.keys())

# Ver las claves con bucle
for clave in dict6.keys():
    print(clave)

# Ver las claves con valores
for valor in dict6.values():
    print(valor)

# Todo junto
for clave, valor in dict6.items():
    print(f'clave: {clave} y valor: {valor}')