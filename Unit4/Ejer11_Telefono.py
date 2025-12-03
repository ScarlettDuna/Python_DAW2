"""
Define una clase Telefono con atributo número
Métodos:
    - telefonear imprime 'llamando'
    - colgar imprime 'colgando'
    - str imprime numero
Define una clase Camara con atributo mpx
    Métodos:
    - fotografiar imprime 'fotografiando'
    - str imprime mpx
Define una clase Reproductor con atributo capacidad
    Métodos:
    - reproducir mp3 imprime 'reproduciendo mp3'
    - reproducir video imprime 'reproduciendo video'
    - str imprime capacidad

Define una clase Móvil que hereda teléfono, cámara, reproductor con constructor y __str__

Define una clase MovilTEST
miMovil = Movil(666123456, 12, 200)
print(dir(miMovil))
print(miMovil))
"""

class Telefono():
    def __init__(self, numero):
        self.numero = numero

    def telefonear(self):
        return "Telefonear"

    def colgar(self):
        return "Colgar"

    def __str__(self):
        return self.numero

class Camara():
    def __init__(self, mpx):
        self.mpx = mpx

    def fotografiar(self):
        return "Fotografiando"

    def __str__(self):
        return self.mpx

class Reproductor():
    def __init__(self, capacidad):
        self.capacidad = capacidad

    def reproducirVideo(self):
        return "Reproduciendo Vídeo"

    def reproducirMP3(self):
        return "Reproduciendo mp3"

    def __str__(self):
        return self.capacidad

class Movil(Telefono, Camara,  Reproductor):
    def __init__(self, numero, mpx, capacidad):
        Telefono.__init__(self, numero)
        Camara.__init__(self, mpx)
        Reproductor.__init__(self, capacidad)

    def __str__(self):
        return "Número {0} \n Cámara {1} \n Capacidad {2}".format(self.numero, self.mpx, self.capacidad)




miMovil = Movil(666123456, 12, 200)
print(dir(miMovil))
print(miMovil)