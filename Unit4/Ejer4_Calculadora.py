# Ejemplo de clase con métodos estáticos
class Calculadora():
    def __init__(self, nombre):
        self.nombre = nombre
    def modelo(self):
        return self.nombre
    @staticmethod
    def sumar(x,y):
        return x+y

calc1 = Calculadora("Anchan")
print("Nombre de la calculadora: ", calc1.modelo() )
print("Llamar al método estático sumar: ", Calculadora.sumar(3,5))

# Uso de funciones
print("Nombre de la calculadora: ", getattr(calc1, "nombre"))
setattr(calc1, 'nombre', 'Jaime')
print("Nombre de la calculadora: ", getattr(calc1, "nombre"))

#¿Existe atributo "nombre"?
print("¿Hay atributo 'nombre'?", hasattr(calc1, 'nombre'))
delattr(calc1, 'nombre')
print("¿Hay atributo 'nombre'?", hasattr(calc1, 'nombre'))