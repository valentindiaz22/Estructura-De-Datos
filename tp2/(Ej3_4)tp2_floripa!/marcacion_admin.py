from marcaciones_admin_abstract import MarcacionesAdminAbstract
from empleado import Empleado
from marcacion import Marcacion
from datetime import date,time
from oficina import Oficina
from marcaciontipo import Marcacion_tipo

class Marcaciones_Admin(MarcacionesAdminAbstract):
    
    def agregar(self, marcacion : Marcacion) -> None:
        """Agrega la marcación pasada por parámetro al final de la lista de marcaciones
        Args:
        marcacion (Marcacion): instancia de clase marcación que se
        va a agregar al final de la lista de marcaciones."""
        self.marcaciones.append(marcacion)

    def empleados(self) -> list:
        """Devuelve todos los empleados de los que se tiene registro de marcación(no repetir
        resultados).
        Returns:
        list: lista formada por las ocurrencias únicas de
        empleados dentro de la lista de marcaciones
        """
        aux=[]
        for marcacion in self.marcaciones:
            if marcacion.empleado in aux:
                pass
            else:
                aux.append(marcacion.empleado)
        return aux
            
    def filtrar_por_empleado(self, empleado: Empleado) -> list:
     """Devuelve todas las marcaciones de un empleado."""
     aux=[]
     for marcacion in self.marcaciones:
        if marcacion.empleado == empleado:
            aux.append(marcacion)
     return aux
     
    def filtrar_por_tipo(self, tipo: Marcacion_tipo) -> list:
     """Devuelve todas las marcaciones del tipo especificado por parámetro."""
     aux=[]
     for marcacion in self.marcaciones:
        if marcacion.tipo==tipo:
            aux.append(marcacion)
     return aux
     

    
    def llegadas_tarde(self) -> list:
     """Devuelve las marcaciones realizadas fuera del horario de ingreso."""
     aux=[]
     for marcacion in self.marcaciones:
        if marcacion.fecha_hora>marcacion.empleado.oficina.hora_entrada and marcacion.fecha_hora<marcacion.empleado.oficina.hora_salida:
            aux.append(marcacion)
        else:
            pass
     return aux

    def ordenar_legajo(self) -> None:
        """Ordena las marcaciones por legajo de empleado y luego por fecha/hora."""
        self.marcaciones=sorted(self.marcaciones, key=lambda p: (p.empleado.legajo,p.fecha_hora))

    def ordenar_apellido_nombre(self) -> None:
        """Ordena las marcaciones por apellido y nombre del empleado, luego por fecha/hora."""
        self.marcaciones=sorted(self.marcaciones, key=lambda p: (p.empleado.apellido, p.empleado.nombre, p.fecha_hora))
    
   


    


