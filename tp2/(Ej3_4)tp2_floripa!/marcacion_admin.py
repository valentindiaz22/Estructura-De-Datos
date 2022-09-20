from marcaciones_admin_abstract import MarcacionesAdminAbstract
from empleado import Empleado
from marcacion import Marcacion
from datetime import date,time
from oficina import Oficina
from marcaciontipo import Marcacion_tipo

class Marcaciones_Admin(MarcacionesAdminAbstract):
    
    def agregar(self, marcacion : Marcacion) -> None:
        self.marcaciones.append(marcacion)

    def empleados(self) -> list:
        aux=[]
        for marcacion in self.marcaciones:
            if marcacion.empleado in aux:
                pass
            else:
                aux.append(marcacion.empleado)
        return aux
            
    def filtrar_por_empleado(self, empleado: Empleado) -> list:
     aux=[]
     for marcacion in self.marcaciones:
        if marcacion.empleado == empleado:
            aux.append(marcacion)
     return aux
     
    def filtrar_por_tipo(self, tipo: Marcacion_tipo) -> list:
     aux=[]
     for marcacion in self.marcaciones:
        if marcacion.tipo==tipo:
            aux.append(marcacion)
     return aux
     

    
    def llegadas_tarde(self) -> list:
     aux=[]
     for marcacion in self.marcaciones:
        if marcacion.fecha_hora>marcacion.empleado.oficina.hora_entrada and marcacion.fecha_hora<marcacion.empleado.oficina.hora_salida:
            aux.append(marcacion)
        else:
            pass
     return aux

    def ordenar_legajo(self) -> None:
        self.marcaciones=sorted(self.marcaciones, key=lambda p: (p.empleado.legajo,p.fecha_hora))

    def ordenar_apellido_nombre(self) -> None:
        self.marcaciones=sorted(self.marcaciones, key=lambda p: (p.empleado.apellido, p.empleado.nombre, p.fecha_hora))
    
   


    


