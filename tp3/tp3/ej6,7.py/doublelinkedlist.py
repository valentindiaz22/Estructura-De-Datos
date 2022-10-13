from typing import Union,Any,Iterator
from list_node import ListNode
from doublelinkedlistabstract import DoubleLinkedListAbstract


class DoubleLinkedList(DoubleLinkedListAbstract):
    def __init__(self) -> None:
        self._head : Union[ListNode, None] = None
        self._size : int = 0
        self._tail : Union[ListNode, None] = None
    
    def __len__(self) -> int:
        """Devuelve la cantidad de elementos que tiene actualmente la lista.
        Returns:
        int: entero que indica a longitud de la lista. 0 si está vacía.
        """
        return self._size
    
    def __getitem__(self, key: int) -> Any:
        """Devuelve el elemento ubicado en la posición indicada por key.
        Args:
        key (int): posición de la que se va a retornar el elemento de la lista.
        Raises:
        Exception: Arroja excepción si el índice está fuera de rango.
        Returns:
        Any: Devuelve el valor ubicado en la posición indicada por key.
        """
        aux2=self._head

        if self.is_empty():
            raise Exception("Operación no permitida si la estructura está vacía.")

        if key>self._size or key<0:
            raise Exception ("Indice fuera de rango")
        else:
            head=self._head
            aux=0
            while head!=None:
                aux+=1
                
                if key==aux:
                    aux2=head.element
                
                head=head.next
                
            return aux2

    
    def __setitem__(self, key: int, value: Any) -> None:
        """En la posición indicada por key se va a colocar value.
        Args:
        key (int): posición que se va a actualizar.
        value (Any): nuevo valor que se va a colocar.
        Raises:
        Exception: Arroja excepción si el índice está fuera de rango.
        """
        if self.is_empty():
            raise Exception("Operación no permitida si la estructura está vacía.")

        if key>self._size or key<0:
            raise Exception ("Indice fuera de rango")
        else:
            head=self._head
            aux=0
            while head!=None:
                aux+=1
                if key==aux:
                    head.element=value
                head=head.next
            
    
    def __delitem__(self, key: int) -> None:
        """Elimina de la estructura el elemento ubicado en la posición key.
        Args:
        key (int): posición cuyo nodo se va a quitar de la estructura.
        Raises:
        Exception: Arroja excepción si el índice está fuera de rango.
        """
        if self.is_empty():
            raise Exception("Operación no permitida si la estructura está vacía.")
        
        if key>self._size or key<0:
            raise Exception ("Indice fuera de rango")
                    
        previo = None
        actual=self._head
        aux=0
        while actual:               
            if key==aux:
                if previo: # Si existe el previo
                    previo.next = actual.next
                    actual.prev = previo
                else: # Si no
                    self._head = actual.next
                    actual.prev = None
            
            previo = actual
            actual = actual.next
            aux += 1
            
        self._size-=1
            

    def __iter__(self) -> Iterator[Any]:
        """ Visita desde el principio hacia el final todos los nodos de la lista y
        retorna sus elementos.
        Yields:
        Iterator[Any]: Cada uno de los elementos de los nodos de lista.
        """
        # aux=[]
        # head=self._head
        # while head!=None:
        #     aux.append(head.element)
        #     head=head.next
        # return aux
        actual = self._head.next
        while actual:
            yield actual.element
            
            actual = actual.next
    
    def __str__(self) -> str:
        """Concatena en un único string todos los elementos de la lista.
        Returns:
        str: string con todos los elementos de la lista convertidos en str.
        """
        if self.is_empty():
            return "DoubleLinkedList()"

        resultado = ""
        actual = self._head
        while actual != None:
            resultado += str(actual.element) + ", "
            actual = actual.next

        resultado = resultado[:len(resultado)-2]
        return f"DoubleLinkedList({resultado})"
    
    def is_empty(self) -> bool:
        """ Indica si la estructura está vacía.
        Returns:
        bool: True si la lista está vacía, caso contrario, False.
        """
        return self._size == 0
    
    def append(self, elem: Any) -> None:
        """ Agrega el elemento pasado por parámetro al final de la lista.
        Args:
        elem (Any): elemento que va a quedar ubicado en la última posición
        """
        nuevo_nodo = ListNode(elem, self._head)
        
        if self.is_empty():
            self._head = nuevo_nodo
            self._tail = nuevo_nodo
        else:
            self._head = nuevo_nodo
            
        self._size += 1
