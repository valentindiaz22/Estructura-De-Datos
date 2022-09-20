class Plataforma:
    def __init__(self,nombre:str,es_portatil:bool) -> None :
        self.nombre=nombre
        if es_portatil==True:
            self.es_portatil="Si"
        else:
            self.es_portatil="No"
    
    def __str__(self) -> str :
        return f"Nombre: {self.nombre}, ¿Es portatil?: {self.es_portatil}"
    
    def __repr__(self) -> str :
        # return f"Plataforma(nombre:{self.nombre},es_portatil:{self.es_portatil})"
        return f"Nombre: {self.nombre}, ¿Es portatil?: {self.es_portatil}"
    
    def __eq__(self,other):
        if isinstance(other, Plataforma):
            return self.nombre==other.nombre
        else:
            print("El objeto no forma parte de Plataforma")