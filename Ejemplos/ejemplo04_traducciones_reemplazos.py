print("{titulo:*^60}".format(titulo = "TRADUCCIONES Y REEMPLAZOS"))

cad1 = "whisper words of wisdom... let it be"

print("{titulo: <20}".format(titulo = "cad1.removeprefix('whisper'):"), cad1.removeprefix('whisper'))
print("{titulo: <20}".format(titulo = "cad1.removesuffix('be'):"), cad1.removesuffix('be'))
print("{titulo: <20}".format(titulo = "cad1.replace('...','🎸'):"), cad1.replace('w','🎸'))
print("_"*20)

