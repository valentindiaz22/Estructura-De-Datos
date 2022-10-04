from list_node import ListNode
from typing import Any, Union
from deque_abstract import DequeAbstract

class Deque(DequeAbstract):
    def __init__(self) -> None:
        self._head : Union[ListNode, None] = None
        self._size : int = 0
        self._tail : Union[ListNode, None] = None

    def __len__(self) -> str:
        """Devuelve la cantidad actual de elementos en la estructura.
        Returns:
        int: Devuelve la cantidad de elementos, cero la si estructura está vacía.
        """

        return self._size
   
    def __str__(self) -> int:
        """ Concatena en un único string todos los elementos almacenados
        en los nodos de la estructura.
        Returns:
        str: convierte en str todos los elementos y los concatena en un string.
         """

        if self.is_empty():
            return "LinkedStack()"

        resultado = ""
        actual = self._head
        while actual != None:
            resultado += str(actual.element) + ", "
            actual = actual.next

        resultado = resultado[:len(resultado)-2]
        return f"LinkedStack({resultado})"
    
    def is_empty(self) -> bool:
        """Indica si la estructura está vacía.
        Returns:
        bool: True si la estructura está vacía, False en caso contrario.
        """

        return self._size == 0
    
    def first(self) -> Any:
        """Devuelve el elemento ubicado en el frente de la estructura.
        Raises:
        Exception: Arroja excepción si la estructura está vacía.
        Returns:
        Any: Devuelve el elemento dato correspondiente al frente de la
        estructura.
        """

        if self.is_empty():
            raise Exception("Pila vacía. Operación no soportada")
        
        return self._head.element
    
    def last(self) -> Any:
        """ Devuelve el elemento correspondiente al nodo ubicado al final de
        la estructura.
        Raises:
        Exception: Arroja excepción si la estructura está vacía.
        Returns:
        Any: Devuelve el elemento dato correspondiente al final de la estructura.
        """

        if self.is_empty():
            raise Exception("Pila vacía. Operación no soportada")
        
        return self._tail.element
    
    def add_first(self, elem : Any) -> None:
        """Agrega un elemento al principio de la estructura.
        Args:
        element (Any): elemento que va a ser agregado al principio de la
        estructura.
        """

        nuevo_nodo = ListNode(elem, None)
        
        if self.is_empty():
            self._head = nuevo_nodo
            self._tail = nuevo_nodo
        else:
            self._head.next = nuevo_nodo
            self._head = self._head.next
            
        self._size += 1
    
    def add_last(self, element : Any) -> None:
        """Agrega un elemento al final de la estructura.
        Args:
        element (Any): elemento que va a ser agregado al final de la estructura.
        """
        
        nuevo_nodo = ListNode(element, None)
        
        if self.is_empty():
            self._head = nuevo_nodo
            self._tail = nuevo_nodo
        else:
            self._tail.next = nuevo_nodo
            self._tail = self._tail.next
            
        self._size += 1
    
    def delete_first(self) -> None:
        """Quita el elemento ubicado en el frente de la estructura.
        Raises:
        Exception: Arroja excepción si la estructura está vacía.
        """

        if self.is_empty():
            raise Exception("Pila vacía. Operación no soportada")
        
        self._head = self._head.next
        self._size -= 1
    
    def delete_last(self) -> None:
        """Quita el elemento ubicado al final de la estructura.
        Raises:
        Exception: Arroja excepción si la estructura está vacía.
        """
        
        if self.is_empty():
            raise Exception("Pila vacía. Operación no soportada")
        
        self._tail = self._tail.next
        self._size -= 1

        
        
        
        
  