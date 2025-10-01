# Variables enteras
x = 3
print(x, "El tipo de x es: ", type(x))

print(x+1); print(x-1); print(x*2); print(x**2)

#Más ejemplos
x+=1
print(x)

x*=2
print(x)

#Floats
y = 2.5
print(y, "El tipo es ", type(y))

#Boolean
t, f = True, False
print(t and f)
print(t or f)
print(not t)
print(t != f)

#Strings - Cadenas
hello = "hello"
world = 'world'
print(hello, world, len(hello))

# Concatenación de cadenas
hw = hello + " " + world
print(hw)

# "control - espacio" muestra la lista de métodos
s= "hello"
print(s.casefold())
print(s.rjust(7)) #Justifica a la derecha con 7 espacios
print(s.replace("ell", "ekk"))
