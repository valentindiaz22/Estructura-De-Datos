from heap_queue import HeapQueue

heap = HeapQueue()

heap.enqueue(15)
heap.enqueue(16)
heap.enqueue(13)
heap.enqueue(1)
heap.enqueue(5)
heap.enqueue(3)
heap.enqueue(25)
heap.enqueue(66)
heap.enqueue(11)
heap.enqueue(5)

print("\n",heap,"\n")
print("Prueba del método len:",heap.__len__(),"\n")
print("Prueba del método is_empty:",heap.is_empty(),"\n")
print("Prueba del método is_full:",heap.is_full(),"\n")
print("Prueba del método first:",heap.first(),"\n")
print("Prueba del método dequeue:",heap.dequeue(),"\n")
print("Metodo enqueue ya probado","\n")
print(heap,"\n")

