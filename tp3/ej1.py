numeros=["(0345)154123456","+5493454123456","3454123456","+54011123456","34564123456"]
print ("Números telefónicos de la ciudad de concordia:")
for item in numeros:
    if item.startswith("(0345)"):
        print (item)
    elif item.startswith("+549345"):
        print (item)
    elif item.startswith("3454"):
        print(item)
    else:
        pass

