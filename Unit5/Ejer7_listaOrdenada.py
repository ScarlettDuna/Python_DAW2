lista1= [1,2,3,4]
lista2= lista1[:]
lista1.sort()
if lista1== lista2:
    print("lista ordenada")
else:
    print("lista no ordenada")