def contarDigitosARG(num):
    # Por si el número introducido no es positivo
    if num < 0:
        num *= -1
    # Caso base
    if num < 10:
        return 1
    # Caso recursivo
    else:   
        return 1 + contarDigitosARG(num // 10)


    
        
print(contarDigitosARG(5))
print(contarDigitosARG(123))
print(contarDigitosARG(10265))