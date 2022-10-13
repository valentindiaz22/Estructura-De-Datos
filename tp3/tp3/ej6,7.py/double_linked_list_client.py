from doublelinkedlist import DoubleLinkedList

doublelinkedlist=DoubleLinkedList()
doublelinkedlist.append("Uno")
doublelinkedlist.append("Dos")
doublelinkedlist.append("Tres")
doublelinkedlist.append("Cuatro")
doublelinkedlist.append("Cinco")
doublelinkedlist.append("Seis")
print("\n",doublelinkedlist,"\n")

print("Longitud:\n",len(doublelinkedlist),"\n")
print("Str:\n",doublelinkedlist,"\n")
print("¿Está vacío?(is_empty):\n",doublelinkedlist.is_empty(),"\n")
print("Item de la posición 3:\n", doublelinkedlist[3],"\n")
doublelinkedlist.__setitem__(3,"Siete")
print("Cambiar item de la posición 3 por Siete:\n",doublelinkedlist,"\n")
print(f"Borrar item de la posición 3 - con valor {doublelinkedlist[3]}:\n")
del doublelinkedlist[2]
print(doublelinkedlist,"\n")
print("Metodo iter:\n")
for i in doublelinkedlist:
    print (i)

