from empleado import Empleado
from marcacion import Marcacion
from marcaciontipo import Marcacion_tipo
from oficina import Oficina
from datetime import time
from marcacion_admin import Marcaciones_Admin

def imprimir(empleados:list):
    print("-"*46)
    for Empleado in empleados:
        print("-"*20)
        print(Empleado.__str__())
    print("-"*46) 

Contabilidad=Oficina("Contabilidad",time(12,00),time(20,00))
Ventas=Oficina("Ventas",time(12,00),time(20,00))

empleado1=Empleado(1,43680773,"Diaz","Valentin",Contabilidad)
empleado2=Empleado(2,17250453,"Rodriguez","Juan",Ventas)
empleado3=Empleado(3,6527656,"Perez","Adolfo",Contabilidad)
empleado4=Empleado(4,40852258,"Fuerte","María",Ventas)
empleado5=Empleado(5,7250111,"Acosta","Roberto",Contabilidad)
empleados=[empleado1,empleado2,empleado3,empleado4,empleado5]

marcacion1=Marcacion(empleado1,time(12,30),Marcacion_tipo.ENTRADA)
marcacion2=Marcacion(empleado2,time(20,00),Marcacion_tipo.SALIDA)
marcacion3=Marcacion(empleado3,time(12,45),Marcacion_tipo.ENTRADA)
marcacion4=Marcacion(empleado4,time(20,00),Marcacion_tipo.SALIDA)
marcacion5=Marcacion(empleado5,time(12,00),Marcacion_tipo.ENTRADA)
marcacion6=Marcacion(empleado1,time(20,00),Marcacion_tipo.SALIDA)
marcacion7=Marcacion(empleado3,time(20,00),Marcacion_tipo.SALIDA)
marcacion8=Marcacion(empleado5,time(20,00),Marcacion_tipo.SALIDA)
marcacion9=Marcacion(empleado2,time(11,45),Marcacion_tipo.ENTRADA)
marcacion10=Marcacion(empleado4,time(12,00),Marcacion_tipo.ENTRADA)
marcacion11=Marcacion(empleado2,time(20,00),Marcacion_tipo.SALIDA)
marcacion12=Marcacion(empleado4,time(20,00),Marcacion_tipo.SALIDA)
marcacion13=Marcacion(empleado1,time(15,10),Marcacion_tipo.ENTRADA)
marcacion14=Marcacion(empleado3,time(12,00),Marcacion_tipo.ENTRADA)
marcacion15=Marcacion(empleado5,time(12,00),Marcacion_tipo.ENTRADA)
marcaciones=Marcaciones_Admin()
marcaciones.agregar(marcacion1)
marcaciones.agregar(marcacion2)
marcaciones.agregar(marcacion3)
marcaciones.agregar(marcacion4)
marcaciones.agregar(marcacion5)
marcaciones.agregar(marcacion6)
marcaciones.agregar(marcacion7)
marcaciones.agregar(marcacion8)
marcaciones.agregar(marcacion9)
marcaciones.agregar(marcacion10)
marcaciones.agregar(marcacion11)
marcaciones.agregar(marcacion12)
marcaciones.agregar(marcacion13)
marcaciones.agregar(marcacion14)
marcaciones.agregar(marcacion15)

print("-"*46)
print("Prueba de método __len__, cantidad de marcaciones:\n",marcaciones.__len__())
print("-"*46)

print("Prueba de método __getitem__, item de la posición 3:\n",marcaciones.__getitem__(3))
print("-"*46)

print("Prueba de método __delitem__, borrar item de la posición 3\n","Item de la posición 3:",marcaciones.__delitem__(3))
print("-"*46)

print("Prueba del método __str__:\n",marcaciones)
print("-"*46)

print("Prueba del método agregar:\n","Reagregar marcación que estaba en la posición 1:\n")
marcaciones.agregar(marcacion4)
print(marcaciones.__getitem__(14))
print("-"*46)

print("Prueba del método empleados:\n"),imprimir(marcaciones.empleados())
print("-"*46)

print("Prueba del método filtrar_por_empleado,prueba con empleado 1:\n")
imprimir(marcaciones.filtrar_por_empleado(empleado1))
print("-"*46)

print("Prueba del método filtrar_por_tipo,prueba con tipo Entrada:\n")
imprimir(marcaciones.filtrar_por_tipo(Marcacion_tipo.ENTRADA))
print("-"*46)

print("Prueba del método llegadas_tarde:\n") 
imprimir(marcaciones.llegadas_tarde())
print("-"*46)

print ("Prueba del método ordenar_legajo:\n")
marcaciones.ordenar_legajo()
imprimir(marcaciones)
print("-"*46)

print("Prueba del método ordenar_apellido_nombre:\n")
marcaciones.ordenar_apellido_nombre()
imprimir(marcaciones)
print("-"*46)






