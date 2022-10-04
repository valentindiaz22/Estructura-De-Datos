from videojuego_admin_abstract import VideojuegosAdminAbstract
from videojuego import Videojuego
from genero import Genero
from plataforma import Plataforma
from empresa import Empresa

class Videojuego_Admin(VideojuegosAdminAbstract):
    
    def __str__(self) -> str:
        """Concatena en un str todos los videojuegos del catálogo."""
        res = ""
        for elem in self.videojuegos:
            res += "{elem}\n".format(elem=str(elem))
        return res

    def agregar(self, videojuego : Videojuego) -> None:
        """Agrega el parámetro al final de videojuegos
        Args:
        videojuego (Videojuego): instancia de clase videojuego que se
        va a agregar al final de la lista de videojuegos.
        """
        self.videojuegos.append(videojuego)
    
    def filtrar_por_desarrolladora(self, desarrolladora: Empresa) -> list:
        """Devuelve los videojuegos desarrollados por la empresa pasada por parámetro."""
        aux=[]
        for Videojuego in self.videojuegos:
            if Videojuego.empresa_desarrolladora==desarrolladora:
                aux.append(Videojuego)
        return aux
        
    def filtrar_por_distribuidora(self, distribuidora: Empresa) -> list:
        """Devuelve los videojuegos distribuídos por la empresa pasada por parámetro."""
        aux=[]
        for Videojuego in self.videojuegos:
            if Videojuego.empresa_distribuidora==distribuidora:
                aux.append(Videojuego)
        return aux

    def filtrar_por_genero(self, genero: Genero) -> list:
        """Devuelve los videojuegos del género pasado por parámetro. """
        aux=[]
        for Videojuego in self.videojuegos:
            if Videojuego.genero==genero:
                aux.append(Videojuego)
        return aux
    
    def cantidad_por_plataforma(self) -> list:
        """Indica la cantidad de videojuegos por plataforma. """
        Windows=0
        Playstation_4=0
        Playstation_5=0
        Xbox_One=0
        Xbox_SeriesX_S=0
        Linux=0
        MacOS=0
        Gba=0
        aux=""
        for Videojuego in self.videojuegos:
            for Videojuego in self.videojuegos:
                for Plataforma in Videojuego.plataforma:
                    if Plataforma.nombre=="Windows":
                        Windows+=1
                    if Plataforma.nombre=="Playstation 4":
                        Playstation_4+=1
                    if Plataforma.nombre=="Playstation 5":
                        Playstation_5+=1
                    if Plataforma.nombre=="Xbox One":
                        Xbox_One+=1
                    if Plataforma.nombre=="Xbox Series X y Series S":
                        Xbox_SeriesX_S+=1
                    if Plataforma.nombre=="Linux":
                     Linux+=1
                    if Plataforma.nombre=="macOS":
                        MacOS+=1
                    if Plataforma.nombre=="Game Boy Advance":
                        Gba+=1
            return [f"Videojuegos en la plataforma Windows: {Windows}\nVideojuegos en la plataforma Playstation 4: {Playstation_4}\nVideojuegos en la plataforma Playstation 5: {Playstation_5}\nVideojuegos en la plataforma Xbox One: {Xbox_One}\nVideojuegos en la plataforma Xbox Series X y Series S: {Xbox_SeriesX_S}\nVideojuegos en la plataforma Linux: {Linux}\nVideojuegos en la plataforma macOS: {MacOS}\nVideojuegos en la plataforma Game Boy Advance: {Gba}\n"]


    def ordenar_titulo(self) -> None:
        """Ordena los videojuegos por titulo."""
        self.videojuegos=sorted(self.videojuegos, key=lambda p: p.titulo)
    
    def ordenar_mejores_primero(self) -> None:
        """Ordena los videojuegos por ranking descendente. """
        self.videojuegos=sorted(self.videojuegos, key=lambda p: p.ranking_metacritic,reverse=True)





    
