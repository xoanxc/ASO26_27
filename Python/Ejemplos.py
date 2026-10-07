""""
variable = "Hola"
pi = 3.14
entero = 10

print(variable)
print(pi)
print(entero)

print(variable + ", " + str(pi) + ", " + str(entero))

valor = "2"
entero = 2

resultado = entero + int(valor)

print(resultado)

# Comentario de una línea
""
Comentario
de
varias
líneas
"""""
"""""
# 1 - Crear un programa que muestre por pantalla cada operación aritmética y sus resultados con valores fijos

suma = 2 + 8
resta = 2 - 8
multiplicacion = 2 * 8
division = 2 / 8

print(suma)
print(resta)
print(multiplicacion)
print(division)

valor1 = int(input("Introduce el valor 1: "))
resultado = valor1 + 2
print(resultado)


# 2 - Crea un programa que solicite dos valores por pantalla. Muestra el resultado de cada operación aritmética básica.

valor1 = int(input("Introduce el valor 1: "))
valor2 = int(input("Introduce el valor 2: "))
suma = valor1 + valor2
resta = valor1 - valor2
multiplicacion = valor1 * valor2
division = valor1 / valor2
print(str(valor1) + " + " + str(valor2) + " = " + str(suma))
print(str(valor1) + " + " + str(valor2) + " = " + str(resta))
print(str(valor1) + " + " + str(valor2) + " = " + str(multiplicacion))
print(str(valor1) + " + " + str(valor2) + " = " + str(division))

if valor1 > valor2:
    print("El valor 1 es mayor que el valor 2")
elif valor1 < valor2:
    print("El valor 1 es menor que el valor 2")
else:
    print("El valor 2 es mayor que el valor 1")

print("Se acaba el if")

valor_1 = int(input("Introduce el valor 1: "))

match valor_1:
    case 1:
        print("El valor es 1")
    case 2:
        print("El valor es 2")
    case 3:
        print("El valor es 3")
    case _:
        print("El valor es 4")

# < menor que
# > mayor que
# == igual que
# != no es igual que

# NOT not lógico

contador = 1
while contador < 10:
    print("El valor es " + str(contador))

for valor in range(0,5):
    print(valor)


import random as rd

aleatorio = rd.randrange(0,100)

print(aleatorio)

import sys

import os

ruta = os.getcwd()
print(ruta)

os.mkdir("/home/iago/Documentos/nuevo")

os.chmod("/home/iago/Documentos/nuevo", 0o777)

os.chown("/home/iago/Documentos/nuevo", 0o777)

import subprocess as sp

sp.run(["ls", "/"])

sp.run(["chmod", "777", "/home/iago/Documentos/nuevo"])

sp.run(["chmod", "root:root", "/home/iago/Documentos/nuevo"])

"""""

lista = [1, 22, 333, 4444, 55555, 666666]

print("--- Lista completa ---")
print(lista)

print("--- Posición mediante indices ---")
print(lista[4])

print("--- Tamaño de la lista ---")
print(len(lista))

print("--- Acceso parcial a la lista ---")
print(lista[0:3])

print("--- Modificar una posición de la lista ---")
lista[0] = 0
print(lista)

print("--- Agregado de valores a la lista ---")
lista.insert(0,1)
print(lista)

print("--- ")
lista.insert(len(lista), 777777)
print(lista)

lista.append(88888888)
print(lista)

lista.remove(88888888)
print(lista)

lista.pop()
print(lista)

lista.pop(4)
print(lista)

del lista[3]
print(lista)

lista.clear()
print(lista)

print("--- Operaciones con listas ---")
for valor in lista:
    print(valor)

for valor in range(len(lista)):
    print(lista[valor])