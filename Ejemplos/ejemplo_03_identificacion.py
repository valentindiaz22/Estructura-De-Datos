print("{titulo:*^60}".format(titulo = "MÉTODOS DE IDENTIFICACIÓN DE CADENAS"))
cad_11 = "11"
cad_225 = "22.5"
cad_hola = "hola"
cad1 = "whisper words of wisdom... let it be"

print("{titulo: <20}".format(titulo = "cad11.isdecimal():"), cad_11.isdecimal())
print("{titulo: <20}".format(titulo = "cad_225.isdecimal():"), cad_225.isdecimal())
print("{titulo: <20}".format(titulo = "cad_hola.isdecimal():"), cad_hola.isdecimal())
print("_"*20)

print("{titulo: <20}".format(titulo = "cad11.isdigit():"), cad_11.isdigit())
print("{titulo: <20}".format(titulo = "cad_225.isdigit():"), cad_225.isdigit())
print("{titulo: <20}".format(titulo = "cad_hola.isdigit():"), cad_hola.isdigit())
print("_"*20)

print("{titulo: <20}".format(titulo = "cad11.isnumeric():"), cad_11.isnumeric())
print("{titulo: <20}".format(titulo = "cad_225.isnumeric():"), cad_225.isnumeric())
print("{titulo: <20}".format(titulo = "cad_hola.isnumeric():"), cad_hola.isnumeric())
print("_"*20)

print("{titulo: <20}".format(titulo = "cad11.isascii():"), cad_11.isascii())
print("{titulo: <20}".format(titulo = "cad_225.isascii():"), cad_225.isascii())
print("{titulo: <20}".format(titulo = "cad_hola.isascii():"), cad_hola.isascii())
print("_"*20)

print("{titulo: <20}".format(titulo = "cad11.isalpha():"), cad_11.isalpha())
print("{titulo: <20}".format(titulo = "cad_225.isalpha():"), cad_225.isalpha())
print("{titulo: <20}".format(titulo = "cad_hola.isalpha():"), cad_hola.isalpha())
print("_"*20)

print("{titulo: <20}".format(titulo = "cad11.isalnum():"), cad_11.isalnum())
print("{titulo: <20}".format(titulo = "cad_225.isalnum():"), cad_225.isalnum())
print("{titulo: <20}".format(titulo = "cad_hola.isalnum():"), cad_hola.isalnum())
print("_"*20)

print("{titulo: <20}".format(titulo = "cad11.isspace():"), cad_11.isspace())
print("{titulo: <20}".format(titulo = "cad_225.isspace():"), cad_225.isspace())
print("{titulo: <20}".format(titulo = "cad_hola.isspace():"), cad_hola.isspace())
print("{titulo: <20}".format(titulo = "' '.isspace():"), ' '.isspace())
print("_"*20)

print("{titulo: <20}".format(titulo = "cad1.islower():"), cad1.islower())
print("{titulo: <20}".format(titulo = "cad1.isupper():"), cad1.isupper())
print("{titulo: <20}".format(titulo = "cad1.istitle():"), cad1.istitle())

print("{titulo: <20}".format(titulo = "cad1.lower().islower():"), cad1.lower().islower())
print("{titulo: <20}".format(titulo = "cad1.upper().isupper():"), cad1.upper().isupper())
print("{titulo: <20}".format(titulo = "cad1.title().istitle():"), cad1.title().istitle())

print("{titulo: <20}".format(titulo = "cad1.startswith('whisper'):"), cad1.startswith('whisper'))
print("{titulo: <20}".format(titulo = "cad1.endswith('be'):"), cad1.endswith('be'))

print("_"*20)