from datetime import datetime

class Videojuego:
    def __init__(self,titulo:str,genero,plataforma:list,descripcion:str,precio:float,empresa_desarrolladora,empresa_distribuidora,fecha_lanzamiento:datetime.time,ranking_metacritic:float) -> None:
        if ranking_metacritic >10 or ranking_metacritic<0:
            raise Exception("Valor incorrecto, ingrese un valor entre 0 y 10.")
        else:
            self.titulo=titulo
            self.genero=genero
            self.plataforma=plataforma
            self.descripcion=descripcion
            self.precio=precio
            self.empresa_desarrolladora=empresa_desarrolladora
            self.empresa_distribuidora=empresa_distribuidora
            self.fecha_lanzamiento=fecha_lanzamiento
            self.ranking_metacritic=ranking_metacritic
    
    def __str__(self) -> str :
        return f"Titulo: {self.titulo}, Genero: {self.genero}, Plataforma: {self.plataforma}\nDescripcion: {self.descripcion}\nPrecio: {self.precio}, Empresa desarrolladora: {self.empresa_desarrolladora}, Empresa distribuidora: {self.empresa_distribuidora}, Fecha de lanzamiento: {self.fecha_lanzamiento}, Ranking de Metacritic: {self.ranking_metacritic}"

    def __repr__(self) -> str :
        return f"Videojuego(titulo:{self.titulo},genero:{self.genero},plataforma:{self.plataforma},descripcion:{self.descripcion},precio:{self.precio},empresa_desarrolladora:{self.empresa_desarrolladora},empresa_distribuidora:{self.empresa_distribuidora},fecha_lanzamiento:{self.fecha_lanzamiento}.ranking_metacritic:{self.ranking_metacritic})"

    def __eq__(self,other):
        if isinstance(other,Videojuego):
            return self.empresa_desarrolladora==other.empresa_desarrolladora and self.titulo ==other.titulo
        else:
            print("El objeto no forma parte de Videojuego")