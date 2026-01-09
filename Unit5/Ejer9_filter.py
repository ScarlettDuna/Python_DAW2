# La función filter construye un iterador con los elementos que cumplen una función
def es_par(num):
    return num % 2 == 0

numeros = [1,2,3,4,5,6,7,8,9,10]

resultado = filter(es_par, numeros)
print(list(resultado))


