from Ejer9_Punto import Punto, Punto3D

p1 = Punto(3, 4)
print("Coordenadas del punto 1: ", p1)
print("¿Qué tiene la clase punto?: ", dir(p1))
miPunto3D = Punto3D(3, 4, 5)
print("¿Qué tiene la clase punto3d?: ", dir(miPunto3D))
otroPunto3D = Punto3D(6, 7, 8)
print("Distancia entre dos puntos 3D: ", miPunto3D.distancia(otroPunto3D))