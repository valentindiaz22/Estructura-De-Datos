class Persona:
    def __init__(self, apellido: str, nombre: str) -> None:
        self.apellido = apellido
        self.nombre = nombre

    def __repr__(self) -> str:
        return "__repr__: Persona(Apellido: {apellido}, Nombre: {nombre})".format(apellido = self.apellido, nombre = self.nombre)
    
    def __str__(self) -> str:
        return "__str__: Persona(Apellido: {apellido}, Nombre: {nombre})".format(apellido = self.apellido, nombre = self.nombre)