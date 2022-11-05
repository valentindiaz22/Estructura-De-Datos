from unsorted_priority_queue_abstract import UnsortedPriorityQueueAbstract
from python_ed_fcad_uner.data_structures.priority_queues import PriorityQueueBase
from typing import Any, Tuple

class UnsortedPriorityQueue(UnsortedPriorityQueueAbstract,PriorityQueueBase):

    def __init__(self):
        self.un_priority_queue = []

    def __len__(self) -> int:
        """ Devuelve la cantidad de elementos en la estructura.
        Returns:
        int: Cantidad de elementos en la estructura. 0 en caso que esté vacía.
        """
        return len(self.un_priority_queue)

    def is_empty(self) -> bool:
        """ Indica si la estructura está vacía o no.
        Returns:
        bool: True si está vacía. False en caso contrario.
        """
        return len(self.un_priority_queue) == 0

    def add(self, k: Any, v: Any) -> None:
        """ Inserta un nuevo ítem al final de la estructura.
        Args:
        k (Any): Clave que determina la prioridad del ítem.
        v (Any): Valor del ítem.
        """
        self.un_priority_queue.append(self._Item(k, v))

    def min(self) -> Tuple[Any]:
        """ Devuelve una tupla conformada por la clave y valor del ítem con menor valor de
        clave.
        Raises:
        Exception: Arroja excepción si se invoca cuando la estructura está vacía.
        Returns:
        Tuple[Any]: Tupla de dos elementos: Clave y Valor del ítem.
        """
        if self.is_empty():
            raise Exception ("Estructura vacía")
        else:
            aux = self.un_priority_queue[0]
            for Item in self.un_priority_queue:
                if Item < aux:
                    aux = Item
            return aux

    def remove_min(self) -> Tuple[Any]:
        """ Quita de la estructura el ítem con menor valor de clave.
        Raises:
        Exception: Arroja excepción si se invoca cuando la estructura está vacía.
        Returns:
        Tuple[Any]: Tupla de dos elementos: Clave y Valor del ítem.
        """
        if self.is_empty():
            raise Exception ("Estructura vacía")
        else:
            aux = self.un_priority_queue[0]

            for Item in self.un_priority_queue:
                if Item < aux:
                    aux = Item

            tupla = (aux._key, aux._value)
            indice = self.un_priority_queue.index(aux)
            del self.un_priority_queue[indice]
            
            
            return tupla
        
    def __str__ (self) -> str:
        """ Retorna todos los items de la lista
        """
        return str(self.un_priority_queue)
        

