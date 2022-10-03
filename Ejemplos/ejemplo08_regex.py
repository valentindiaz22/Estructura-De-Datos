import re

# Todo string que comience con b y al que le sigue cualquier caracter cualquier número de veces.

patron = "^b.*"
print("Patrón:", patron)
print('re.findall(patron, "buen día!"', re.findall(patron, "buen día!"))
print('re.findall(patron, "Buen día!"', re.findall(patron, "Buen día!", flags=re.IGNORECASE))
print('re.findall(patron, "Buen día!"', re.findall(patron, "Buen día!"))
print('re.findall(patron, "buenas tardes!"',re.findall(patron, "buenas tardes!"))

patron = "gracias!$"  # Todo string que termine con gracias!
print("Patrón:", patron)
print('re.findall(patron, "Gracias!"', re.findall(patron, "Gracias!", flags=re.IGNORECASE))
print('re.findall(patron, "Todavía tengo gracias!"',re.findall(patron, "Todavía tengo gracias!"))
print('re.findall(patron, "Gracias! Ahora paso"',re.findall(patron, "Gracias! Ahora paso"))

# Son patentas válidas las que tienen tres letras, un espacio y tres números
patron = "[A-Z]{3}\s[0-9]{3}"
print("Patrón:", patron)
print('re.findall(patron, "ABC 123"', re.findall(patron, "ABC 123", flags=re.IGNORECASE))
print('re.findall(patron, "PYT 310"', re.findall(patron, "PYT 310", flags=re.IGNORECASE))
print('re.findall(patron, "AAA 1212 3BCD 456789"', re.findall(patron, "AAA 1212 3BCD 456789", flags=re.IGNORECASE))
print('re.findall(patron, "AAAA 123"', re.findall(patron, "AAAA 123", flags=re.IGNORECASE))

# Son patentas válidas las que tienen tres letras, un espacio y tres números
patron = "^[A-Z]{3}\s[0-9]{3}$"
print("Patrón:", patron)
print('re.findall(patron, "ABC 123"', re.findall(patron, "ABC 123", flags=re.IGNORECASE))
print('re.findall(patron, "PYT 310"', re.findall(patron, "PYT 310", flags=re.IGNORECASE))
print('re.findall(patron, "AAA 1212 3BCD 456789"', re.findall(patron, "AAA 1212 3BCD 456789", flags=re.IGNORECASE))
print('re.findall(patron, "AAAA 123"', re.findall(patron, "AAAA 123", flags=re.IGNORECASE))

# Son patentas válidas las que tienen tres letras, un espacio y tres números
patron = "^\w{3}\s\d{3}$"
print("Patrón:", patron)
print('re.search(patron, "ABC 123"', re.search(patron, "ABC 123", flags=re.IGNORECASE).span())
print('re.search(patron, "PYT 310"', re.search(patron, "PYT 310", flags=re.IGNORECASE))
print('re.search(patron, "A12 3BCD"', re.search(patron, "A12 3BCD", flags=re.IGNORECASE))

patron = "^([A-Z|a-z]+[,-\\.\\*]+[0-9]+)$"
print("Patrón:", patron)
print('re.search(patron, "abc.1234"', re.findall(patron, "abc.1234"))
print('re.search(patron, "inovello.2022"', re.findall(patron, "inovello.2022"))
print('re.search(patron, "Inovello.2022"', re.findall(patron, "Inovello.2022"))
print('re.search(patron, "abc.1234"', re.findall(patron, "1234.abc"))

ciencia = ["Hipatia de Alejandría (370-416)",
           "Sophie Germain (1776-1831)",
           "Augusta Ada Byron, condesa de Lovelace (1815-1852)",
           "Marie Curie (1867-1934)",
           "Lise Meitner (1878-1968)",
           "Emmy Noether (1882-1935)",
           "Barbara McClintock (1902-1992)",
           "Rosalind Franklin (1920-1958)",
           "Jane Goodall (1934-)",
           "Joselyn Bell (1943-)"]

patron = "([\w|\s,]+)\s\((\d+)-(\d*)\)"
for item in ciencia:
    match = re.match(patron, item, flags=re.IGNORECASE)
    if match:
        print("Científica: {} - Nació: {} - Falleció: {}".format(match.groups()[0], match.groups()[1], match.groups()[2]))
