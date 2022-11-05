from python_ed_fcad_uner.data_structures import LinkedBinaryTree
from linked_binary_tree_abstract import LinkedBinaryTreeExtAbstract
from python_ed_fcad_uner.data_structures import BinaryTreeNode
from typing import Any, List, Union

class LinkedBinaryTreeExt(LinkedBinaryTree, LinkedBinaryTreeExtAbstract):

    def hermanos(self, nodo1 : BinaryTreeNode, nodo2: BinaryTreeNode) -> bool:
        """ Indica si node1 y node2 son hermanos.
        Args:
        nodo1 (BinaryTreeNode): nodo que debe pertenecer al árbol.
        nodo2 (BinaryTreeNode): nodo que debe pertenecer al árbol.
        Returns:
        bool: True si los nodos tienen el mismo padre, False en caso contrario.
        """
        if self._search_parent(nodo1) == self._search_parent(nodo2):
            return True
        else:
            return False

    def hojas(self) -> List[Any]:
        """ Devuelve los elementos de los nodos que no tienen ningún hijo.
         Returns:
        List[Any]: lista formada por los elementos de los nodos hoja.
        """
        lista = []
        for nodo in self.__iter__():
            if nodo.children_count() == 0:
                lista.append(nodo.element)
        return lista



    def internos(self) -> List[Any]:
        """ Devuelve los elementos de los nodos que tienen padre y algún hijo.
        Returns:
        List[Any]: lista formada por los elementos de los nodos internos.
        """
        lista = []
        for nodo in self.__iter__():
            if self._search_parent(nodo):
                if nodo.children_count() > 0:
                    lista.append(nodo.element)
        return lista
    
    def profundidad(self, nodo : BinaryTreeNode) -> int:
        """ Devuelve la longitud del camino entre la raíz y un nodo.
        Args:
        nodo (BinaryTreeNode): nodo del que se quiere conocer la profundidad.
        Returns:
        int: devuelve el número de arcos entre la raíz y nodo. 0 si nodo es la raíz.
        """
        cont = 1
        aux = self._search_parent(nodo)

        if aux == None:
            return 0

        while self._search_parent(nodo):
            aux = self._search_parent(aux)
            if aux == None:
                return cont
            else:
                cont += 1
        return cont

        

    def altura(self, nodo : BinaryTreeNode) -> int:
        """ Retorna la longitud del camino entre nodo y la hoja más lejana.
        Args:
        nodo (BinaryTreeNode): nodo del que se quiere conocer la altura.
        Returns:
        int: Devuelve 0 en caso que nodo sea hoja, caso contrario, la cantidad de arcos
        entre nodo y la hoja más lejana.
        """
        return self._max_height(nodo)-1
        #por como está hecho el método recursivo, si no le sumo 1 al final de _max_height no funciona, asi que le resto uno acá para que quede con el valor correcto.

    def _max_height(self, nodo : BinaryTreeNode) -> int: 

        if nodo == None:
            return 0
            
        izq = self._max_height(nodo.left_child)
        der = self._max_height(nodo.right_child)

        if izq > der:
            return (izq + 1)
        else:
            return (der + 1)
        

        

    

