import random
def num_random(inf,sup):
   return random.randint(inf,sup)
def pensamiento():
    return int(input("Intente adivinar en que número estoy pensando, estoy pensando en: "))   
def comparación(x,z):
    while x!=z:
        if x>z:
            print("El número en el que pienso es mayor")
            z=pensamiento()
        else:
            print("El número en el que pienso es menor")
            z=pensamiento()
    print("Correcto, has ganado!!")            



inf=int(input("Ingrese el límite inferior: "))
sup=int(input("Ingrese el límite superior: "))
x=num_random(inf,sup)
z=pensamiento()
comparación(x,z)

