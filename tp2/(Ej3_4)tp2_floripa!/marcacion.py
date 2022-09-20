from datetime import datetime
from logging import exception
from empleado import Empleado
class Marcacion:
    __NUM_REGISTRO=0
    def __init__(self,empleado:Empleado,fecha_hora:datetime.time,tipo) -> None:
        self.__NUM_REGISTRO=self.__class__.__NUM_REGISTRO
        self.empleado=empleado
        self.fecha_hora=fecha_hora
        self.tipo=tipo
        self.__class__.__NUM_REGISTRO+=1
        
    @property
    def num_registro(self)->int:
        return self.__NUM_REGISTRO

    @num_registro.setter
    def num_registro(self):
        raise Exception("Este atributo no se puede modificar")


    def __str__(self) -> str:
        return f"Número de registro: {self.num_registro}, Empleado: {self.empleado},\nFecha y hora: {self.fecha_hora}, Tipo: {self.tipo.__str__()}\n"    
    def __repr__(self) -> str:
        return f"Marcacion(num_registro:{self.num_registro},empleado:{self.empleado},fecha_hora{self.fecha_hora},tipo:{self.tipo}"
    
    def __eq__(self,other):
        if isinstance(other, Marcacion):
            return self.num_registro==other.num_registro
        else:
            print("El objeto no forma parte de Marcacion")
    

    