from unsorted_priority_queue import UnsortedPriorityQueue

queue=UnsortedPriorityQueue()
queue.add(15,3)
queue.add(1,6)
queue.add(17,15)
queue.add(1,5)
queue.add(15,1)
queue.add(3,2)

print ("\n",queue,"\n")
print ("Prueba método __len__:",queue.__len__(),"\n")
print ("Prueba método is_empty:",queue.is_empty(),"\n")
print ("Método add ya probado","\n")
print ("Prueba del método min:",queue.min(),"\n")
print ("Prueba del método remove_min:",queue.remove_min(),"\n")
print (queue,"\n")