# 5 - Crea un programa que permita al usuario introducir valores hasta que introduzca un valor negativo. Mostrar la media de todos los valores introducidos y el número de valores.
import math

valor = 0
contador = 0
valorTotal = 0
mediaTotal = 0
maximo = -math.inf
minimo = math.inf

while valor > -1:
    valor = int(input("Ingrese un número: "))

    if valor > -1:
        contador = contador + 1
        valorTotal = valorTotal + valor
        mediaTotal = valorTotal/contador

print("La media de todos los valores es: " + str(mediaTotal))
print("El número de valores introducidos es: " + str(contador))