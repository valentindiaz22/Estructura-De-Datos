from pq_stack import PriorityQueueStack

priority_stack= PriorityQueueStack()
priority_stack.push(23)
priority_stack.push(15)
priority_stack.push(65)
priority_stack.push(23)
priority_stack.push(3)

print("\n",priority_stack,"\n")
print("Prueba del método pop:",priority_stack.pop(),"\n")
print("Método push ya probado","\n")
print("Prueba del método is_empty:",priority_stack.is_empty(),"\n")
print("Prueba del método top:",priority_stack.top(),"\n")
print(priority_stack,"\n")