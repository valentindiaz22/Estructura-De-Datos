from persona import Persona

print("{titulo:*^60}".format(titulo = "FORMATEO SIMPLE"))

print("* Las llaves '{' y '}' son reemplazadas por los valores pasados a format en el orden que aparecen.")
print("Mi banda favorita es {}! 馃馃馃".format("Foo Fighters"))
print("{0} era un {1} que vivia muy fel铆z!".format("Bartolito", "Gallo"))
print()
###############

print("{titulo:*^60}".format(titulo = "OTRO TIPO DE STRINGS"))
emoji = "馃槑"

print("* string normal: Impresi贸n: {emoji}")
test_str = "Impresi贸n: {emoji}"
print(test_str)

print("* Si anteponemos la letra f a un string entonces har谩 la interpolaci贸n:")
test_str = f"Impresi贸n: {emoji}"
print(test_str)
print()
###############

print("{titulo:*^60}".format(titulo = "FORMATEO ALTERANDO EL ORDEN"))
print("* Si dentro de las llaves ponemos nombre par谩metros podemos reemplazar por nombre.")
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
print("* Por defecto la impresi贸n de objetos es utilizando __str__()")
print("Impresi贸n: {persona}".format(persona=persona))

print("* Con !s especificamos que use __repr__() para dar formato")
print("Impresi贸n: {persona!s}".format(persona=persona))

print("* Con !r especificamos que use __repr__() para dar formato")
print("Impresi贸n: {persona!r}".format(persona=persona))
print()