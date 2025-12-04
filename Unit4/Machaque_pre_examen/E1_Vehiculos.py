class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
    def arrancar(self):
        return "El vehículo está arrancado."
    # Getter y Setter -> Marca
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    # Getter y Setter -> Modelo
    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    # Getter y Setter -> Velocidad Máxima
    @property
    def velocidad_maxima(self):
        return self._velocidad_maxima
    @velocidad_maxima.setter
    def velocidad_maxima(self, velocidad_maxima):
        if velocidad_maxima > 0:
            self._velocidad_maxima = velocidad_maxima
        else:
            raise ValueError("La velocidad máxima debe ser positiva")

    def __str__(self):
        return f"Este es un vehiculo marca {self.marca} modelo {self.modelo} con velocidad máxima {self.velocidad_maxima} km/h."

class Coche(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima):
        super().__init__(marca, modelo, velocidad_maxima)
    def arrancar(self):
        return f"El coche {self.marca} está arrancando con suavidad"
    def abrir_maletero(self):
        return "Maletero abierto."

class Moto(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima):
        super().__init__(marca, modelo, velocidad_maxima)
    def arrancar(self):
        return f"La moto {self.marca} ruge al arrancar"
    def hacer_caballito(self):
        return "Toma caballito!"

class Camion(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, capacidad_carga):
        super().__init__(marca, modelo, velocidad_maxima)
        self.capacidad_carga = capacidad_carga

    # Getter y Setter -> capacidad_carga
    @property
    def capacidad_carga(self):
        return self._capacidad_carga

    @capacidad_carga.setter
    def capacidad_carga(self, capacidad_carga):
        if capacidad_carga > 0:
            self._capacidad_carga = capacidad_carga
        else:
            raise ValueError("La capacidad de carga debe ser positiva")