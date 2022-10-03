from persona import Persona

print("{titulo:*^60}".format(titulo = "FORMATEO SIMPLE"))

print("* Las llaves '{' y '}' son reemplazadas por los valores pasados a format en el orden que aparecen.")
print("Mi banda favorita es {}! 🤘🤘🤘".format("Foo Fighters"))
print("{0} era un {1} que vivia muy felíz!".format("Bartolito", "Gallo"))
print()
###############

print("{titulo:*^60}".format(titulo = "OTRO TIPO DE STRINGS"))
emoji = "😎"

print("* string normal: Impresión: {emoji}")
test_str = "Impresión: {emoji}"
print(test_str)

print("* Si anteponemos la letra f a un string entonces hará la interpolación:")
test_str = f"Impresión: {emoji}"
print(test_str)
print()
###############

print("{titulo:*^60}".format(titulo = "FORMATEO ALTERANDO EL ORDEN"))
print("* Si dentro de las llaves ponemos nombre parámetros podemos reemplazar por nombre.")
print("In times like these you learn to live again. In times like this".format("La vaca Lola", "cola", "cabeza"))

print("{titulo:*^60}".format(titulo = "OTRO TIPO DE STRINGS"))
valor = "love"
print(f'''All you need is {valor}
All you need is {valor}
All you need is {valor}, {valor}
{valor} is all you need''')
print()

###############

print("{titulo:*^60}".format(titulo = "FORMATEO DE OBJETOS"))

persona = Persona("Grohl", "Dave")
print("* Por defecto la impresión de objetos es utilizando __str__()")
print("Impresión: {persona}".format(persona=persona))

print("* Con !s especificamos que use __repr__() para dar formato")
print("Impresión: {persona!s}".format(persona=persona))

print("* Con !r especificamos que use __repr__() para dar formato")
print("Impresión: {persona!r}".format(persona=persona))
print()