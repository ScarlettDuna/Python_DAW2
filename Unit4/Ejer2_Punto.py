"""
Representación de un punto en un plano, atributos X & Y
Los métodos especiales empiezan y terminan con __
Los atributos de objeto se inicializan en el constructor llamado __init__()

"""
import math


class Punto():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def mostrar(self):
        print(self.x, ", ", self.y)
    def distancia(self, otra_x, otra_y):
        dis = math.sqrt((otra_x - self.x)**2 + (otra_y - self.y)**2)
        return round(dis, 2)
    def distancia_puntos(self, punto):
        dis = math.sqrt((punto.x - self.x)**2 + (punto.y - self.y)**2)
        return round(dis, 2)

punto1 = Punto()
punto1.mostrar()
punto2 = Punto(4, 5)
punto2.mostrar()
print("Distancia entre punto1 y punto2", punto1.distancia_puntos(punto2))

punto3 = Punto(3,4)
print("Distancia entre (3,4) y (7,1)", punto3.distancia(7,1))
