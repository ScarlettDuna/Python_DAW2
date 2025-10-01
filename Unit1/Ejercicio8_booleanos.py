# True se representa como 1 y False como 0
print(1 == False)
print(0.0 == False)
print(True + True)
print(not True)
print(True and False)
print(True or False)
a = 15; b = 10
print(f"\n comparando a={a} y b{b}")
print(f"¿Es a mayor que b? :{a>b}")
print(f"¿Es a igual que b? :{a==b}")
print(f"¿Es distinto que b? :{a!=b}")

condicion1 = a>b
condicion2 = a==b

#función any que comprueba si algún número de una lista es positivo
numeros = [-5, 2, 0, 10, -8]
hay_alguno_positivo = any(numeros)
print(hay_alguno_positivo)