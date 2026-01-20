with open("files/temperaturas.txt", "r") as temperaturas:
    with open("files/tempsMayor20.txt", "w", encoding="utf-8") as tempsMayor20:
        lineas = temperaturas.readlines()
        for linea in lineas:
            if float(linea) > 20:
                tempsMayor20.write(linea)