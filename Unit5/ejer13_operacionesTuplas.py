datos_persona=("Ana",30,"Madrid")
nombre=datos_persona[0]
print(f"Nombre: {nombre}")

#último elemento
ciudad=datos_persona[2]
print(f"Ciudad: {ciudad}")
ciudad=datos_persona[-1]
print(f"Ciudad: {ciudad}")

#desempaquetado
tupla1 =1,2,3
a,b,c=tupla1

print("Valor de a:",a)
nuevaTupla=tupla1+(4,)
print("Tupla1:",nuevaTupla)

tupla2=(1,2,3,4,5,1,5,4,3,5,2,6)

#contar1
print("¿Cuantos 1 hay en la tupla?")
print(tupla2.count(1))

print("Posicion del num 2")
print(tupla2.index(2))


print("Posición del otro 1")
print(tupla2.index(1,2))
print("Posición del otro 1 entre 2 y 6") #test
print(tupla2.index(1,2,6))