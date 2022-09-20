def conteoas(cont):    
     if cont=="ascendente":
      lim=int(input("Ingrese el límite superior: "))
      for i in range(lim+1): 
       if i>=1: 
        print(i)
def conteodes(cont):    
     if cont=="descendente":
      lim=int(input("Ingrese el límite inferior (menor que 20): "))
      aux=20
      while aux>=lim and aux>=1 and lim<=20: 
        print(aux)
        aux-=1
      if lim>20:
        print("Ingrese un valor menor o igual que 20")    
 
cont=str(input("Ingrese si desea un conteo ascendente o descendente: ")) 
if cont=="ascendente" or cont=="descendente":
    if cont=="ascendente":
        conteoas(cont)
    else:
     conteodes(cont)
else:
    print("Incorrecto. No se puede continuar")
 



