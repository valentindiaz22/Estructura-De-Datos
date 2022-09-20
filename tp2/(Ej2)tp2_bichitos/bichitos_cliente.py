from especie import Especie
from mascota import Mascota
from persona import Persona
from raza import Raza

def imprimir(mascotas:list):
    for Mascota in mascotas:
        print("-"*46)
        print(Mascota.__str__())
    print("-"*46) 

def filtrar_gerontes(mascotas:list):
    aux=[]
    for Mascota in mascotas:
        if Mascota.edad>=13:
            aux.append(Mascota)
    return aux

def filtrar_por_especie(mascotas:list,especie:Especie):
    aux=[]
    for Mascota in mascotas:
        if especie==Mascota.raza.especie:
            aux.append(Mascota)
    return aux

def max_mascotero(mascotas:list):
    aux=0
    for Mascota in mascotas:
        persona=Mascota.dueño
        for Mascota in mascotas:
            mayor=0
            if persona==Mascota.dueño:
                mayor+=1
            if mayor>aux:
                aux=mayor
                persona_aux=persona
    return persona_aux

mascota1=Mascota(20,"Sol",Raza("Border_Collie",Especie("Perro")),2017,Persona("Mendiburu","Esperanza","45666420"))
mascota2=Mascota(14,"Nova",Raza("Collie",Especie("Perro")),2021,Persona("Martinez","Paula","12435680"))
mascota3=Mascota(25,"Luna",Raza("Border_Collie",Especie("Perro")),2005,Persona("Perez","Julián","40999123"))
mascota4=Mascota(4,"Negrita",Raza("Mestiza",Especie("Perro")),2019,Persona("Alvarez","Pedro","10223654"))
mascota5=Mascota(17,"Sami",Raza("Pastor_Alemán",Especie("Perro")),2015,Persona("Chavez","Tomás","22258680"))
mascota6=Mascota(87,"Mel",Raza("Siamés",Especie("Gato")),2020,Persona("Mendiburu","Esperanza","45666420"))
mascotas=[mascota1,mascota2,mascota3,mascota4,mascota5,mascota6]
  
print("-"*46) 
print("Lista total de mascotas:")
imprimir(mascotas)

mascotas_mayores=filtrar_gerontes(mascotas)
print("\nMascotas mayores o con 13 años:")
imprimir(mascotas_mayores)

especie=Especie("Gato")
filtrado_especie=filtrar_por_especie(mascotas,especie)
print("\nMascotas de la Especie Gato:")
imprimir(filtrado_especie)

mayor_mascotero=max_mascotero(mascotas)
print("\nLa persona con mayor cantidad de mascotas a su cargo es:")
print("-"*46) 
print(mayor_mascotero)
print("-"*46) 
