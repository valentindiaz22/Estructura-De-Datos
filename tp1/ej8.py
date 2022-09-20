def crear_ciudades (ciudades):
    preg=str(input("¿Desea agregar más ciudades?: "))
    if preg=="Si" or preg=="No" or preg=="si" or preg=="no":
        while preg == "Si" or preg=="si":
            ciudad=str(input("Ingrese el nombre de una ciudad que desee conocer: "))
            ciudades.append(ciudad)
            preg=str(input("¿Desea agregar más ciudades?: "))
        print("La cantidad de ciudades cargadas es de:",len(ciudades),", las ciudades ingresadas son:",ciudades )
    else:
        print("Ingrese una respuesta válida,(Si o No) ")
          
                    

a=str(input("Ingrese el nombre de una ciudad que desee conocer: "))
b=str(input("Ingrese el nombre de una ciudad que desee conocer: "))
c=str(input("Ingrese el nombre de una ciudad que desee conocer: "))
ciudades=[a,b,c]
crear_ciudades(ciudades)
