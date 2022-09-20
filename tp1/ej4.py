def comparador_num(num1):
 while num1>20 or num1<10:
  if num1<10:
    num1=int(input("Valor inferior, ingrese nuevamente: "))
  if num1>20:
    num1=int(input("Valor superior, ingrese nuevamente: "))
 print("Gracias!!!")

    
num1=int(input("Ingrese un número entre 10 y 20: "))
comparador_num(num1)
