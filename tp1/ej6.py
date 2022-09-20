def generador_colores(inicio,fin):
 if inicio>=0 and inicio<=4:
    if fin>=5 and fin<=9:
        coloresnew=colores[inicio:fin]
        print(coloresnew)
    else:
        print("Ingrese un valor válido")
 else:
    print("Ingrese un valor válido")

colores=['Azul', 'Verde', 'Rojo', 'Amarillo', 'Violeta', 'Rosa','Negro', 'Celeste', 'Gris', 'Blanco']
inicio=int(input("Ingrese el número de inicio(entre 0 y 4): "))
fin=int(input("Ingrese el número de fin(entre 5 y 9: "))
generador_colores(inicio,fin)


