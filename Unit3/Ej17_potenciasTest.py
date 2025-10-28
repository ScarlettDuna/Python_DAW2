# Para importar de otra clase
import Ejercicio17_potencias
print(dir(Ejercicio17_potencias)) #imprime las funciones que tenemos definidas
print(Ejercicio17_potencias.cuadrado(3))

# Se puede usar alias
import Ejercicio17_potencias as p
print(p.cubo(3))

# podemos importar varios elementos separados por comas
from Ejercicio17_potencias import cubo, cuadrado
# poner alias
from Ejercicio17_potencias import cubo as pcubo
from Ejercicio17_potencias import cuadrado as pcuad
print(pcubo(3))
print(pcuad(4))