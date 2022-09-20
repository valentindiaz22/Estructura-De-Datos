class Libro:
    def __init__(self,n_inv:int,titulo:str,autor,categoria,anio_publicacion:int)-> None:
        self.n_inv=n_inv
        self.titulo=titulo
        self.autor=autor
        self.categoria=categoria
        self.anio_publicacion=anio_publicacion

    def __str__(self)-> str:
        return f"Número de inventario: {self.n_inv}, Titulo: {self.titulo}, Autor: {self.autor}, Categoria: {self.categoria}, Año de publicación: {self.anio_publicacion}"

    def __eq__(self,other):
        if isinstance(other,Libro):
            return self.n_inv==other.n_inv
        else:
            print("El objeto no forma parte de Libro")
