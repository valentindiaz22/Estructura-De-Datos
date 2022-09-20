from oficina import Oficina
class Empleado:
    def __init__(self,legajo:int,documento:str,apellido:str,nombre:str,oficina:Oficina) -> None:
        self.legajo=legajo
        self.documento=documento
        self.apellido=apellido
        self.nombre=nombre
        self.oficina=oficina
    
    def __str__(self) -> str:
        return f"Número de legajo: {self.legajo}, Número de documento: {self.documento},\nApellido: {self.apellido}, Nombre: {self.nombre}, Oficina: {self.oficina}"

    def __repr__(self) -> str:
        return f"Empleado(legajo={self.legajo},documento={self.documento},apellido={self.apellido},nombre={self.nombre},oficina={self.oficina}\n"

    def __eq__(self,other):
        if isinstance(other,Empleado):
            return self.legajo==other.legajo
        else:
            print("El objeto no forma parte de empleado")

    def __lt__(self,other):
        if isinstance(other,Empleado):
            return self.legajo<other.legajo
        else:
            print("El objeto no forma parte de empleado")
