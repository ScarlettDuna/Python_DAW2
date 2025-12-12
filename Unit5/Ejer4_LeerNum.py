# Leer un número por pantalla
num=int(input("Número: "))
lista = []
while num >= 0:
    lista.append(num)
    num = int(input("Número: "))

print("Y el mayor de la lista es: %d" %max(lista))

for n in lista:
    if n % 2 == 0:
        print(n, end=" ")