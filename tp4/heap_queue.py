from python_ed_fcad_uner.data_structures.priority_queues.array_heap import ArrayHeap
from typing import Any

class HeapQueue():

    DEFAULT_CAPACITY : int = 10

    def __init__(self,) -> None:
        self.heap = ArrayHeap()
        self.instancia = 0

    
    def __len__(self) -> int:
        """Devuelve el número de elementos en la estructura.

        Returns:
            int: entero que indica la cantidad actual de elementos almacenados en la estructura. 
        """
        return len(self.heap)
    
    def is_empty(self) -> bool:
        """Indica si el heap está vacío

        Returns:
            bool: True si el heap está vacio, False en caso contrario
        """
        return len(self.heap) == 0
    
    def is_full(self) -> bool:
        """Indica si la estructura está llena.

        Returns:
            bool: True si se llenó, caso contrario False
        """
        return self.__class__.DEFAULT_CAPACITY == len(self.heap)
    
    def first(self) -> Any:
        """Devuelve (sin quitar) el elemento ubicado en el frente del Heap."

        Raises:
            Exception: Arroja excepción si la estructura está vacía.

        Returns:
            Any: Devuelve el elemento más antigüo en orden de inserción.
        """
        
        if self.is_empty(): 
            raise Exception("Estructura vacía. No se puede continuar")
        
        aux = self.heap.min()
        return aux[1]
    
    def dequeue(self) -> Any:
        """Remueve y devuelve el primer elemento del heap.

        Returns:
            Any: valor ubicado en el frente de la estructura.
        """
        if self.is_empty():
            raise Exception("Estructura vacía. No se puede continuar")
        
        aux = self.heap.remove_min()
        return aux[1]
    
    def enqueue(self, elem: Any) -> None:
        """Agrega un elemento al final de la estructura.

        Args:
            elem (Any): Nuevo elemento al final de la estructura.

        Raises:
            Exception: Arroja excepción si la estructura está llena.
        """
        if self.is_full():
            raise Exception ("Estructura llena. No se puede continuar")
        
        self.heap.add(self.instancia,elem)
        self.instancia += 1

    def __str__(self) -> str:
        return str(self.heap)
        
        

    
