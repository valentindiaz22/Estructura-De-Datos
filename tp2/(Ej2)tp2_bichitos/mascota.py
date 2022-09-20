class Mascota:
    __ANIO_ACTUAL=2022
    def __init__(self,n_registro:int,nombre:str,raza,anio_nacimiento:int,dueño) -> None:
        self.n_registro=n_registro
        self.nombre=nombre
        self.raza=raza
        self.anio_nacimiento=anio_nacimiento
        self.dueño=dueño

    @property
    def edad(self)-> int:
        edad=self.__class__.__ANIO_ACTUAL-self.anio_nacimiento
        return edad
         
    def __str__(self) -> str:
        return f"Número de registro: {self.n_registro}, Nombre: {self.nombre}, Raza: {self.raza}\nAño de nacimiento: {self.anio_nacimiento}, Dueño: {self.dueño}"

    def __repr__(self) -> str:
        return f"Mascota(n_registro:{self.n_registro},nombre:{self.nombre},raza:{self.raza},anio_nacimiento:{self.anio_nacimiento}),dueño:{self.dueño}"
    
    def __eq__(self,other):
        if isinstance(other,Mascota):
            return self.n_registro==other.n_registro
        else:
            print("El objeto no forma parte de Mascota")
        