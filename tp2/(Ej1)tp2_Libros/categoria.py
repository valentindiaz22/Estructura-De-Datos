class Categoria:
    def __init__(self,nombre:str) -> None:
        self.nombre=nombre
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}"

    def __eq__(self,other):
        if isinstance(other,Categoria):
            return self.nombre==other.nombre
        else:
            print("El objeto no forma parte de Categoría")