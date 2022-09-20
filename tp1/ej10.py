def agregar_persona(dic_empleado):
    legajo=int(input("Ingrese el número de legajo: "))
    apellido=str(input("Ingrese el apellido: "))    
    nombre=str(input("Ingrese el nombre: "))
    camisa=int(input("Ingrese el talle de camisa: "))
    pantalon=int(input("Ingrese el talle de pantalón: "))
    aux=str(input("Ingrese si utiliza o no zapatos de seguridad: "))
    if aux=="si" or aux=="Si" or aux=="No" or aux=="no":
        if aux=="si" or aux=="Si":
            zapatos=True
        else:
            zapatos=False    
    else:
        print("Ingrese un valor válido, Si o No")
        aux=str(input("Ingrese si utiliza o no zapatos de seguridad: "))  
    agregar_dic(legajo,apellido,nombre,camisa,pantalon,zapatos,dic_empleado)

def quitar_persona(dic_empleado):
    auxiliar=0
    for i in dic_empleado:
        print(auxiliar,":",dic_empleado[auxiliar],"\n")
        auxiliar+=1
    eliminar=int(input("Ingrese el número de la persona a eliminar: "))
    del dic_empleado[eliminar]
    menus=int(input("¿Como desea continuar?: \n""1-Agregar otro empleado \n""2-Quitar un empleado \n""3-Ordenar la lista por legajo \n""4-Ordenar la lista por apellido y nombre \n""5-Imprimir lista y salir \n""********************\n",))
    menu(menus,dic_empleado)


def agregar_dic(legajo,apellido,nombre,camisa,pantalon,zapatos,dic_empleado):
    empleado={"legajo": legajo,"apellido":apellido,"nombre":nombre,"camisa":camisa,"pantalon":pantalon,"zapatos":zapatos}
    dic_empleado.append(empleado)
    print("*"*20)
    menus=int(input("¿Como desea continuar?: \n""1-Agregar otro empleado \n""2-Quitar un empleado \n""3-Ordenar la lista por legajo \n""4-Ordenar la lista por apellido y nombre \n""5-Imprimir lista y salir \n""********************\n",))
    menu(menus,dic_empleado)

def ordenar_legajo(dic_empleado):
    dic_empleado= sorted(dic_empleado, key=lambda p: p["legajo"])
    auxiliar=0
    for i in dic_empleado:
     print(auxiliar,":",dic_empleado[auxiliar],"\n")
     auxiliar+=1 

def ordenar_apellido_nombre(dic_empleado):
    dic_empleado= sorted(dic_empleado, key=lambda p: p["apellido"]) #No encontramos forma de ordenarlo por nombre a la vez, si utilizamos "and p["nombre"]", solo lo ordena por nombre.
    auxiliar=0
    for i in dic_empleado:
     print(auxiliar,":",dic_empleado[auxiliar],"\n")
     auxiliar+=1 

def cerrar_menu(dic_empleado):
    auxiliar=0
    for i in dic_empleado:
     print(auxiliar,":",dic_empleado[auxiliar],"\n")
     auxiliar+=1    

def menu(menus,dic_empleado):
    print("\n")   
    if menus==1:
        agregar_persona(dic_empleado)
    if menus==2:
        quitar_persona(dic_empleado)
    if menus==3:
        ordenar_legajo(dic_empleado)  
    if menus==4:
        ordenar_apellido_nombre(dic_empleado)
    if menus==5:
        cerrar_menu(dic_empleado)    
      
dic_empleado=[
    {"legajo": 345,"apellido":"Rodriguez","nombre":"Juan","camisa":45,"pantalon":67,"zapatos":False},
    {"legajo": 567,"apellido":"Diaz","nombre":"Valentin","camisa":36,"pantalon":32,"zapatos":False},
    {"legajo": 123,"apellido":"Gonzales","nombre":"Roberto","camisa":22,"pantalon":34,"zapatos":True}
]           
print("*" *20)
menus=int(input("¿Como desea continuar?: \n""1-Agregar otro empleado \n""2-Quitar un empleado \n""3-Ordenar la lista por legajo \n""4-Ordenar la lista por apellido y nombre \n""5-Imprimir lista y salir \n""********************\n",))
menu(menus,dic_empleado)

#Ejercicio hecho con Francisco Bordagaray