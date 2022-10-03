print("{titulo:*^60}".format(titulo = "MÉTODOS RELACIONADOS CON EL TAMAÑO DE LETRA"))
cad1 = "whisper words of wisdom... let it be"

print("{titulo:_^20}".format(titulo = "cad1.lower():"))
print(cad1.lower())

print("{titulo:_^20}".format(titulo = "cad1.upper():"))
print(cad1.upper())

print("{titulo:_^20}".format(titulo = "cad1.title():"))
print(cad1.title())

print("{titulo:_^20}".format(titulo = "cad1.capitalize():"))
print(cad1.capitalize())

print("{titulo:_^20}".format(titulo = "cad1.swapcase():"))
print(cad1.capitalize().swapcase())

print("{titulo:_^20}".format(titulo = "cad1.casefold():"))
print(cad1.casefold())