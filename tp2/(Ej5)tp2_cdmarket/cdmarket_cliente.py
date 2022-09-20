from datetime import datetime
from empresa import Empresa
from genero import Genero
from plataforma import Plataforma
from videojuego import Videojuego
from videojuego_admin import Videojuego_Admin

def imprimir(videojuegos:list):
    print("-"*46)
    for Videojuego in videojuegos:
        print("-"*20)
        print(Videojuego.__str__())
    print("-"*46) 

videojuego1=Videojuego("Red Dead Redemption 2",Genero.Accion_aventuras,[Plataforma("Windows",False),Plataforma("Playstation 4",False),Plataforma("Playstation 5",False),Plataforma("Xbox One",False),Plataforma("Xbox Series X y Series S",False)],"Al igual que la primera entrega, Red Dead Redemption 2 es un juego de acción y aventura, jugado tanto como primera como tercera persona, ambientado en el lejano oeste estadounidense y desarrollado en un entorno de mundo abierto con una versión ficticia del oeste",2499,Empresa("Rockstar Games"),Empresa("Rockstar Games"),datetime(2018,10,26),9.7)
videojuego2=Videojuego("Potion Craft",Genero.Otro,[Plataforma("Windows",False),Plataforma("Linux",False)],"Potion Craft es un simulador de alquimista en el que interactúa físicamente con sus herramientas e ingredientes para elaborar pociones.",179.99,Empresa("niceplay games"),Empresa("tinyBuild"),datetime(2021,9,21),7.6)
videojuego3=Videojuego("Dirt 4",Genero.Carreras,[Plataforma("Windows",False),Plataforma("Playstation 4",False),Plataforma("Xbox One",False),Plataforma("macOS",False),Plataforma("Linux",False)],"Dirt 4 es un videojuego de carreras centrado en el rally. Los jugadores compiten en eventos de etapa cronometrados en asfalto y terreno todoterreno en condiciones climáticas variables.",224.99,Empresa("Codemasters"),Empresa("Codemasters"),datetime(2017,6,9),8.5)
videojuego4=Videojuego("The Legend of Zelda: Breath of the Wild",Genero.Accion_aventuras,[Plataforma("Nintendo Switch",True)],"El jugador controla a Link, que despierta en un mundo postapocalíptico después de estar cien años durmiendo para derrotar a Ganon y salvar al reino de Hyrule.",6680,Empresa("Nintendo"),Empresa("Nintendo"),datetime(2017,3,3),9.7)
videojuego5=Videojuego("Pokemon Rubí",Genero.Rpg,[Plataforma("Game Boy Advance",True)],"El protagonista comienza su aventura con un Pokémon y puede capturar más con pokebolas, con el objetivo de luchar contra otros Pokémon, ya sean salvajes o con entrenadores.",4400,Empresa("Game Freak"),Empresa("Nintendo"),datetime(2002,11,21),8.2)
videojuegos=Videojuego_Admin()
videojuegos.agregar(videojuego1)
videojuegos.agregar(videojuego2)
videojuegos.agregar(videojuego3)
videojuegos.agregar(videojuego4)
videojuegos.agregar(videojuego5)

print("-"*46)
print("Prueba del metodo __len__:",videojuegos.__len__())
print("-"*46)

print("-"*46)
print("Prueba del método __getitem__:\n","Item de la posición 0:\n",videojuegos.__getitem__(0))
print("-"*46)

print("-"*46)
print("Prueba del método __delitem__:\n","Item de la posición 1:",videojuegos.__delitem__(1))
print("-"*46)

print("-"*46)
print("Prueba del método __str__:\n",videojuegos)
print("-"*46)

print("-"*46)
print("Prueba del método agregar:\n","Reagregar juego que estaba en la posición 1:\n")
videojuegos.agregar(videojuego2)
print(videojuegos.__getitem__(4))
print("-"*46)

print("-"*46)
print("Prueba del método filtrar_por_desarrolladora:\n","Videojuegos de la desarrolladora Rockstar Games:")
imprimir(videojuegos.filtrar_por_desarrolladora(Empresa("Rockstar Games")))
print("-"*46)

print("-"*46)
print("Prueba del método filtrar_por_distribuidora:\n","Videojuegos de la distribuidora Nintendo:\n")
imprimir(videojuegos.filtrar_por_distribuidora(Empresa("Nintendo")))
print("-"*46)

print("-"*46)
print("Prueba del método filtrar_por_genero:\n","Videojuegos del genero Carreras:\n")
imprimir(videojuegos.filtrar_por_genero(Genero.Carreras))
print("-"*46)

print("-"*46)
print("Prueba del método cantidad_por_plataforma:\n")
Windows=Plataforma("Windows",True)
imprimir(videojuegos.cantidad_por_plataforma())
print("-"*46)

print("-"*46)
print("Prueba del método ordenar_titulo:\n")
videojuegos.ordenar_titulo()
imprimir(videojuegos)
print("-"*46)

print("-"*46)
print("Prueba del método ordenar_mejores_primero:\n")
videojuegos.ordenar_mejores_primero()
imprimir(videojuegos)
print("-"*46)








