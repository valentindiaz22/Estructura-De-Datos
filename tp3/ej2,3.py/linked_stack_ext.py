from typing import Any
from linked_stack import LinkedStack
from linked_abstract import LinkedStackExtAbstract



class LinkedStackExt(LinkedStackExtAbstract,LinkedStack):
    def multi_pop(self, num: int) -> list[Any]:
        """Realiza la cantidad de operaciones pop() indicada por num.
        Args:
        num (int): número de veces que se va a ejecutar pop().
        Raises:
        Exception: Arroja excepción si se invoca a pop() por cuando la estructura
        está vacía.
        Returns:
        List[Any]: lista formada por todos los topes que se quitaron de la pila.
        """
        while num>0:
                if self.is_empty():
                    raise Exception("Pila vacía. Operación no soportada")

                resultado = self._head.element
                self._head = self._head.next
                self._size -= 1
                res=[]
                res.append(resultado)
                num+=-1
        return res


    def replace_all(self, param1: Any, param2: Any) -> None:
        """Reemplaza todas las ocurrencias de param1 en la pila por param2.
        Args:
        param1 (Any): Valor a buscar/reemplazar.
        param2 (Any): Nuevo valor.
        """
        aux=self._head
        while aux:
            if aux.element==param1:
                aux.element=param2
            aux=aux.next

    def exchange(self) -> None:
        """Intercambia el elemento ubicado en el tope con el más antigüo o último.
        Raises:
        Exception: Arroja excepción si la estructura está vacía.
        """
        if self.is_empty():
            raise Exception("Pila vacía. Operación no soportada")

        head=self._head
        aux=self.top()
        while head!=None:
            if head.next==None:
                tail=head.element
                head.element=aux
            head=head.next
        self._head.element=tail
                

            

