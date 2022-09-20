from autor import Autor
from categoria import Categoria
from libro import Libro

def imprimir(libros:list):
    print("-"*46)
    for Libro in libros:
        print(Libro.__str__())
    print("-"*46) 

def filtrar_por_categoria(libros:list,cat:Categoria) -> list:
    aux=[]
    for Libro in libros:
        if Libro.categoria==cat:
            aux.append(Libro)
    return aux

def filtrar_por_autor(libros: list, autor:Autor) -> list:
    aux=[]
    for Libro in libros:
        if Libro.autor==autor:
            aux.append(Libro)
    return aux

def filtrar_por_anio(libros: list, anio : int) -> list:
    aux=[]
    for Libro in libros:
        if Libro.anio_publicacion==anio:
            aux.append(Libro)
    return aux


libro1 = Libro(64,"El principito",Autor("Antoine","de Saint-Exupery"),Categoria("Novela infantil"),1943)
libro2 = Libro(23, "Los juegos del hambre",Autor("Suzanne","Collins"),Categoria("Aventura"),2008) 
libro3 = Libro(150,"Harry Potter y la piedra filosofal",Autor("J. K.", "Rowling"),Categoria("Fantasía"),1997)
libro4 = Libro(10,"En llamas",Autor("Suzanne","Collins"),Categoria("Aventura"),2009)
libro5 = Libro(17,"Sinsajo",Autor("Suzanne","Collins"),Categoria("Aventura"),2010)

libros=[libro1,libro2,libro3,libro4,libro5]
print("\n Lista total de libros en la biblioteca:")
imprimir(libros)

cat=Categoria("Aventura")
filtro_cat=filtrar_por_categoria (libros,cat)
print("Filtrado por la categoría Aventura:")
imprimir(filtro_cat)

autor=Autor("J. K.", "Rowling")
filtro_au=filtrar_por_autor(libros,autor)
print("Filtrado por la autora J. K. Rowling:")
imprimir(filtro_au)

anio=int(1943)
filtro_anio=filtrar_por_anio(libros,anio)
print("Filtrado por libros publicados en el año 1943:")
imprimir(filtro_anio)







