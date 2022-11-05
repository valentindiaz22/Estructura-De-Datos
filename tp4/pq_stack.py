from python_ed_fcad_uner.data_structures.priority_queues import PriorityQueueBase
from typing import Any

class PriorityQueueStack (PriorityQueueBase):
    def __init__(self) -> None:
        """ Constructor
        """
        self.priority_stack = []
        self.instancia = 0

    def push(self, v : Any) -> None:
        """Agrega un item al final de la pila
        """
        self.priority_stack.append(self._Item(self.instancia,v))
        self.instancia -= 1 
    
    def pop(self) -> Any:
        """Quita el item al final de la pila
        Arroja una excepción si la pila está vacía
        """
        if self.is_empty():
            raise Exception("La pila está vacía")

        return self.priority_stack.pop()
    
    def is_empty(self) -> bool:
        """Retorna un booleano indicando si la pila está vacía o no
        """
        return len(self.priority_stack) == 0
    
    def __str__(self) -> str:
        """ Retorna todos los items de la pila
        """
        return str(self.priority_stack)
    
    def top(self) -> Any:
        """Muestra el item al final de la pila (Sin removerlo)
        Arroja una excepción si la pila está vacía
        """
        if self.is_empty():
            raise Exception("La pila está vacía. La operación no se puede llevar a cabo.")

        return self.priority_stack[-1]


    