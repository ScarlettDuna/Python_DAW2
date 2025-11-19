# Primera clase (Se nombran en mayúsculas)
class Clase():
    # atributo de clase
    at_clase = 1
    # método que referencia al objeto que utiliza este método
    def metodo(self):
        # atributo del método y por tanto del objeto y no de la clase
        self.at_objeto = 1

# Crear un objeto de la clase
objeto = Clase()
print(type(objeto))

# Vamos a ver el valor del atributo de la clase
print("Atributo de la clase", Clase.at_clase)
# Para ver el valor del atributo del objeto tengo que llamar al método que crea el atributo
objeto.metodo() # una vez inicializado el valor del atributo del objeto, puedo mostrarlo
print("Atributo del objeto ", objeto.at_objeto)