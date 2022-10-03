print("{titulo:*^60}".format(titulo="MANIPULACIÓN DE CADENAS LIMPIADO, DIVISIÓN Y UNIÓN"))

cad1 = "   whisper words of wisdom... let it be   "

print("{titulo: <20}".format(titulo="cad1:"), cad1)
print("{titulo: <20}".format(titulo="cad1.strip():"), cad1.strip())
print("{titulo: <20}".format(titulo="cad1.rstrip():"), cad1.rstrip())
print("{titulo: <20}".format(titulo="cad1.lstrip():"), cad1.lstrip())
print("_"*20)
print('\n🎸'.join(['And when the night is cloudy', 'There is still a light that shines on me', "Shine on 'til tomorrow", 'Let it be']))
