class Persona:
    def __init__(self,apellido:str,nombre:str,documento:str) -> None:
        self.apellido=apellido
        self.nombre=nombre
        self.documento=documento
    
    def __str__(self) -> str:
        return f"Apellido: {self.apellido}, Nombre: {self.nombre}, Documento: {self.documento}"

    def __repr__(self) -> str:
        return f"Persona(apellido:{self.apellido},nombre:{self.nombre},documento:{self.documento})"

    def __eq__(self,other):
        if isinstance(other, Persona):
            return self.documento==other.documento
        else:
            print("El objeto no forma parte de Persona")
    