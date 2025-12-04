class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    # Getter y Setter -> Nombre
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str):
            self._nombre = nombre
        else:
            raise ValueError ("El nombre debe ser texto")

    # Getter y Setter -> Email
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        if isinstance(email, str) and '@' in email:
            self._email = email
        else:
            raise ValueError("El email debe ser texto y tiene que tener un '@'.")

    def saludar(self):
        return f"Hola, soy {self.nombre}"
    def __str__(self):
        return f"Este usuario se llama {self.nombre} y su email es {self.email}"

class Alumno(Usuario):
    def __init__(self, nombre, email, curso):
        super().__init__(nombre, email)
        self.curso = curso

    # Getter y Setter -> Curso
    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        if isinstance(curso, int):
            self._curso = curso
        else:
            raise ValueError("El curso debe ser un número")

    def saludar(self):
        return f"Hola, soy {self.nombre}, alumno del {self.curso}"

class Profesor(Usuario):
    def __init__(self, nombre, email, departamento):
        super().__init__(nombre, email)
        self.departamento = departamento

    # Getter y Setter -> Departamento
    @property
    def departamento(self):
        return self._departamento

    @departamento.setter
    def departamento(self, departamento):
        if isinstance(departamento, str):
            self._departamento = departamento
        else:
            raise ValueError("El nombre del departamento debe ser texto")
    def saludar(self):
        return f"Buenos días, soy el profesor {self.nombre} del departamento de {self.departamento}"

class Administrador(Usuario):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)

    def saludar(self):
        return f"Soy {self.nombre}, administrador del sistema"

    def banear(self, usuario):
        return f"El usuario {usuario.nombre} ha sido bloqueado"
