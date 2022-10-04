from deque import Deque


deque=Deque
deque.add_first("Uno")
deque.add_first("Dos")
deque.add_first("Tres")
print("Deque con 3 elementos agregados desde el head:\n",deque)
deque.add_last("Cuatro")
deque.add_last("Cinco")
deque.add_last("Seis")
print("Deque con 3 elementos agregados desde el tail:\n",deque)
print("Longitud:\n",deque.__len__())
print("Str:\n",deque.__str__())
print("¿Está vacío?(is_empty):\n",deque.is_empty())
print("Primer elemento:\n",deque.first())
print("Ultimo elemento:\n",deque.last())
print("Borrar el primer elemento:\n",deque.delete_first())
print(deque)
print("Borrar el último elemento:\n",deque.delete_last())
print(deque)

