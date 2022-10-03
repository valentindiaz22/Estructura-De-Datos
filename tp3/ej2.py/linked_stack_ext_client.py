from linked_stack_ext import LinkedStackExt


pila=LinkedStackExt()
pila.push("Uno")
pila.push("Dos")
pila.push("Tres")
pila.push("Cuatro")
pila.push("Cinco")
pila.push("Seis")
print("El elemento en el top es:",pila.top())
print("La longitud de la pila es:",pila.__len__())
print("Pila default:\n",pila)
pila.multi_pop(3)
print("Pila luego de 3 pops:\n",pila)
pila.replace_all("Uno","Siete")
print("Pila luego de 3 pops y cambiando Uno por Siete:\n",pila)
pila.exchange()
print("Pila luego de implementar el metodo exchange:\n",pila)
