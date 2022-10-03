print("{titulo:*^60}".format(titulo = "MÉTODOS DE BÚSQUEDA Y CONTEO"))
cad1 = "Whisper words of wisdom... Let it be"

print("{titulo:_^20}".format(titulo = "cad1.count():"))
print(cad1.count("."))

print("{titulo:_^20}".format(titulo = "cad1.find():"))
print(cad1.find("."))

print("{titulo:_^20}".format(titulo = "cad1.index():"))
print(cad1.index("."))

print("{titulo:_^20}".format(titulo = "cad1.find() vs cad1.index():"))
print(cad1.find("x"))
try:
    print(cad1.index("x"))
except:
    print("no se enconntró ninguna x")