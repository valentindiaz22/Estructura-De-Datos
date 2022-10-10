from doublelinkedlist import DoubleLinkedList

doublelinkedlist=DoubleLinkedList()
doublelinkedlist.append("Uno")
doublelinkedlist.append("Dos")
doublelinkedlist.append("Tres")
doublelinkedlist.append("Cuatro")
doublelinkedlist.append("Cinco")
doublelinkedlist.append("Seis")
print(doublelinkedlist)
print("Longitud:\n",doublelinkedlist.__len__(),"\n")
print("Str:\n",doublelinkedlist.__str__(),"\n")
print("¿Está vacío?(is_empty):\n",doublelinkedlist.is_empty(),"\n")
print("Item de la posición 3:\n",doublelinkedlist.__getitem__(3),"\n")
doublelinkedlist.__setitem__(3,"Siete")
print("Cambiar item de la posición 3 por Siete:\n",doublelinkedlist,"\n")
print("Borrar item de la posición 3:\n")
# doublelinkedlist.__delitem__(3) Método que no puedo implementar, me toma el item como NoneType, supongo que es un error con el prev pero no pude descrifrar dónde está el problema
print(doublelinkedlist,"\n")
print("Metodo iter:\n")
for i in doublelinkedlist:
    print (i)

