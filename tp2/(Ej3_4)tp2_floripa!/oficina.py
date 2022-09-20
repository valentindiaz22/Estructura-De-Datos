from datetime import datetime

class Oficina:
    def __init__(self,nombre:str,hora_entrada:datetime.time,hora_salida:datetime.time) -> None:
        self.nombre=nombre
        self.hora_entrada=hora_entrada
        self.hora_salida=hora_salida
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Hora de entrada: {self.hora_entrada}, Hora de salida: {self.hora_salida}"

    def __repr__(self) -> str:
        return f"Oficina(Nombre={self.nombre},hora_entrada={self.hora_entrada},hora_salida={self.hora_salida}"
    
    def __eq__(self,other):
        if isinstance(other,Oficina):
            return self.nombre==other.nombre
        else:
            print("El objeto no forma parte de Oficina")
        