class Punto():
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    #Definimos una propiedad para obtener el valor de x
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @x.setter
    def x(self, x):
        self._x = x
    @y.setter
    def y(self, y):
        self._y = y
    def __str__(self):
        return "{0}:{1}".format(self.x, self.y)
    def distancia(self, otro):
        dx = self.x - otro.x
        dy = self.y - otro.y
        return (dx ** 2 + dy ** 2) ** 0.5

class Punto3D(Punto):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    @property
    def z(self):
        return self._z
    @z.setter
    def z(self, valor):
        self._z = valor
    def __str__(self):
        return super().__str__() + ":" + str(self.z)
    def distancia(self, otro):
        dx = self.x - otro.x
        dy = self.y - otro.y
        dz = self.z - otro.z
        return (dx ** 2 + dy ** 2 + dz ** 2) ** 0.5