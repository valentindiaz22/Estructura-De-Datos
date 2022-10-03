from typing import Any
from linked_stack import LinkedStack
from linked_abstract import LinkedStackExtAbstract



class LinkedStackExt(LinkedStackExtAbstract,LinkedStack):
    def multi_pop(self, num: int) -> list[Any]:
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
        aux=self._head
        while aux:
            if aux.element==param1:
                aux.element=param2
            aux=aux.next

    def exchange(self) -> None:
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
                
        # while aux!=None:
        #     aux2=aux
        #     aux=aux.next
        # self.pop()
        # self.push(aux2)
    


            

