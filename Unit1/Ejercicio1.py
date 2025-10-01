#Ejemplo de 1 clase
edad = 23
#Cada bloque de instrucciones debe estar tabulado
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


num = 3
if num >= 0:
    while num < 10:
        print(num)
        num = num + 1

# El punto y coma (;) se puede usar para separar varias sentencias en una línea
edad = 15; print(edad)

# Si el bloque a tabular se escribe en una sola línea, se puede escribir después de los dos puntos
azul = True
if azul: print("Cielo")

# Lo que vaya entre paréntesis o corchetes puede ocupar varias líneas
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes",
        "Sábado", "Domingo"]
print(dias)