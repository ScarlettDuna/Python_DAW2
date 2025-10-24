def calculadoraXXX(*numeros, operador, redondear=False):
    if not numeros:
        print("No se han proporcionado datos")
        return None
    if operador not in ["suma", "media", "max", "min"]:
        print("Error: operación no válida");
        return None
    resultado = 0
    match operador:
        case "suma":
            for item in numeros:
                resultado += item
        case "media":
            contador = 0
            total = 0
            for item in numeros:
                total += item
                contador += 1
            resultado = total / contador
        case "max":
            resultado = numeros[0]
            for item in numeros:
                if item > resultado:
                    resultado = item
        case "min":
            resultado = numeros[0]
            for item in numeros:
                if item < resultado:
                    resultado = item

    if redondear:
        return round(resultado, 2)
    return resultado


print(calculadoraXXX(10, 20, 15, operador="resta"))
print(calculadoraXXX(5, 9, 25, operador="media"))
print(calculadoraXXX(-5, 4, 28.5, operador="media", redondear=True))
print(calculadoraXXX(2, -9, 6, operador="max"))
print(calculadoraXXX(2, 4, -6, operador="min"))

