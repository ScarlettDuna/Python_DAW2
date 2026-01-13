#las cadenas son secuencias de caracteres: Inmutable
cad="Hola"
cad2="¿Qué tal"
cad3='''Hola
        qué tal'''
print(cad,cad2,cad3)

#también se pueden crear cadenas con str a partir de otros tipos de datos
cad4=str(1)
cad5=str(2.45)
cad6=str([1,2,3])

print(cad4,cad5,cad6)
print("a">"A") #test

cad7="aloha, alohaaaaa"
print(cad7.capitalize())

cad8="Hola Mundo"
print(cad8.lower())
print(cad8.swapcase())

cad9="Aloha que tal bb jeje"
print(cad9.swapcase().title())
print(cad9.center(50)) #tabula50 espacios
print(cad9.ljust(50,"-"))
print(cad9.rjust(50,"-"))

#busqueda
cad10="bienvenidas a mi isla"
print("a", cad10.count("a"))
print("a", cad10.count("a",16))
print("Posición de mi",cad10.find("mi"))
print(cad10.startswith("b"))
print(cad10.endswith("a"))


#SUSTITUCION
cad11="Estimado señor nombre apellido: "
buscar="nombre apellido"
cambiar_por="Juan Perez"
print(cad11.replace(buscar,cambiar_por))

cad11Aux=cad11[5:9]
cad11Aux2=cad11[5:]
print("Cad11aux",cad11Aux)
print("Cad11aux",cad11Aux2)
cad11Aux3=cad11[::-1]
print("Cad11aux",cad11Aux3)

risas = "ja"*3
print(risas)

cad12 = "00000000000123000000"
print(cad12.strip("0"))

cad1 = "Hola"
print()