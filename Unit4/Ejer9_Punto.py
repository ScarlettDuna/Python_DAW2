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

