class Autor:
    def __init__(self,nombre:str,apellido:str) -> None:
        self.nombre=nombre
        self.apellido=apellido

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}"
    
    def __eq__(self,other):
        if isinstance(other, Autor):
            return self.nombre == other.nombre and self.apellido == other.apellido
        else:
            print("El objeto no forma parte de Autor")


