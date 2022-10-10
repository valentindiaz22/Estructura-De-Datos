import re
numeros=["(0345) 154123456","+5493454123456","3454123456","+54011123456","34564123456"]
patron="\\(0345\\)\s[0-9]{2}[0-9]{7}|\\+549345[0-9]{7}|^345[0-9]{7}$"
print("Patrón:", patron)
for item in numeros:
    print(re.findall(patron, item))

# print ("Números telefónicos de la ciudad de concordia:")
# for item in numeros:
#     if item.startswith("(0345)"):
#         print (item)
#     elif item.startswith("+549345"):
#         print (item)
#     elif item.startswith("3454"):
#         print(item)
#     else:
#         pass

# primera versión, funcionaba pero no usaba el paquete re