def agregar_platos(a,b,c,d):
    comida[1]=a
    comida[2]=b
    comida[3]=c
    comida[4]=d
    print(comida)
def quitar_platos(comida,erase):
    if erase==1:
     del comida[1]
     print(comida)
    if erase==2:
     del comida[2]
     print(comida)
    if erase==3:
     del comida[3]
     print(comida)
    if erase==4:
     del comida[4]
     print(comida)     
      
comida={}        
a=str(input("Ingrese su primer plato favorito: "))
b=str(input("Ingrese su segundo plato favorito: "))
c=str(input("Ingrese su tercer plato favorito: "))
d=str(input("Ingrese su cuarto plato favorito: "))
agregar_platos(a,b,c,d)
erase=int(input("Ingrese la clave del plato que desee eliminar: "))
quitar_platos(comida,erase)

