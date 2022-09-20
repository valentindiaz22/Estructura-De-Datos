class Raza:
    def __init__(self,nombre:str,especie) -> None:
        self.nombre=nombre
        self.especie=especie
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Especie: {self.especie}"

    def __repr__(self) -> str:
        return f"Raza(nombre:{self.nombre},especie:{self.especie})"
    
    def __eq__(self,other):
        if isinstance(self,other):
            return self.nombre==other.nombre
        else:
            print("El objeto no forma parte de Raza")
