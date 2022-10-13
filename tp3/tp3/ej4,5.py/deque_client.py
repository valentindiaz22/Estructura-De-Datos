from deque import Deque


deque=Deque()
deque.add_first("Uno")
deque.add_first("Dos")
deque.add_first("Tres")
print("Deque con 3 elementos agregados desde el head:\n",deque,"\n")
deque.add_last("Cuatro")
deque.add_last("Cinco")
deque.add_last("Seis")
print("Deque con 3 elementos agregados desde el tail:\n",deque,"\n")
print("Longitud:\n",len(deque),"\n")
print("Str:\n",deque.__str__(),"\n")
print("¿Está vacío?(is_empty):\n",deque.is_empty(),"\n")
print("Primer elemento:\n",deque.first(),"\n")
print("Ultimo elemento:\n",deque.last(),"\n")
print("Borrar el primer elemento:\n")
deque.delete_first()
print(deque)
print("Borrar el último elemento:\n")
deque.delete_last()
print(deque,"\n")

