#range: tipo de secuencia que permita crear secuecias rangos de numeros

#inmutable, se suele utilizar para bucles

rango=range(0,10,2)
print(type(rango))
print(rango)
print(list(rango)) #TEST

#PROPIEDADES DE RANGO
print("Inicio: ",rango.start)
print("Fin: ",rango.stop)
print("Intervalo: ",rango.step)
print("Rango de 0,9", list(range(0,10,1)))
print("Rango de 1,11", list(range(1,12)))
print("Rango mult 5 hasta 30",list(range(0,30,5)))
print("Rango mult 0 hasta -10",list(range(0,-10,-1)))

for i in range(11):
    print(i,end="")