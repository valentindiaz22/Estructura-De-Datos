def nuevo_num(lista,nuevo):
   if nuevo>=100 and nuevo<=999: 
    if nuevo in lista:
        print("Se encuentra en la lista, en la posición:",lista.index(nuevo))
    else:
        print("El valor ingresado no es parte de la lista")
   else:
    print("El número no tiene 3 dígitos")     

lista=[111,222,333,444]
for i in lista:
    print(i)
nuevo=int(input("Ingrese un número de 3 dígitos: "))
nuevo_num(lista,nuevo)
