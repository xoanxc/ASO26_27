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

Comentarios
de
varias
líneas


# 1 - Crear un programa que muestre por pantalla cada operación aritmética y sus resultados con valores fijos


valor_1 = 5
valor_2 = 7

resultado = valor_1 + valor_2

print(str(valor_1) + " + " + str(valor_2) + " = " + str(resultado))

resultado = valor_1 - valor_2

print(str(valor_1) + " - " + str(valor_2) + " = " + str(resultado))

resultado = valor_1 * valor_2

print(str(valor_1) + " * " + str(valor_2) + " = " + str(resultado))

resultado = valor_1 / valor_2

print(str(valor_1) + " / " + str(valor_2) + " = " + str(resultado))

resultado = valor_1 % valor_2

print(str(valor_1) + " % " + str(valor_2) + " = " + str(resultado))

valor_1 = int(input("Introduce el valor 1: "))
resultado = valor_1 + 2
print(resultado)

# 2 - Crea un programa que solicite dos valores por pantalla. Muestra el resultado de cada operación aritmética básica

valor_1 = int(input("Introduce el primer valor: "))
valor_2 = int(input("Introduce el segundo valor: "))

resultado = valor_1 + valor_2
print(str(valor_1) + " + " + str(valor_2) + " = " + str(resultado))

resultado = valor_1 - valor_2
print(str(valor_1) + " - " + str(valor_2) + " = " + str(resultado))

resultado = valor_1 * valor_2
print(str(valor_1) + " * " + str(valor_2) + " = " + str(resultado))

resultado = valor_1 / valor_2
print(str(valor_1) + " / " + str(valor_2) + " = " + str(resultado))

resultado = valor_1 % valor_2
print(str(valor_1) + " % " + str(valor_2) + " = " + str(resultado))


valor_1 = int(input("Introduce el primer valor: "))
valor_2 = int(input("Introduce el segundo valor: "))

if valor_1 > valor_2:
    print("El valor 1 es mayor que el valor 2")
elif valor_1 < valor_2:
    print("El valor 2 es mayor que el valor 1")
else:
    print("Los valores son iguales")

print("Se acaba el if")

valor_1 = int(input("Introduce el primer valor: "))

match valor_1:
    case 1:
        print("El valor es 1")
    case 2:
        print("El valor es 2")
    case 3:
        print("El valor es 3")
    case _:
        print("No es ninguno de los valores aceptados")

valor_1 = input("Introduce el primer valor: ")

match valor_1:
    case "azul":
            print("El color es azul")
    case "blanco":
            print("El color es blanco")
    case _:
            print("Opción no válida")

# < - menor que
# > - mayor que
# == - igual que
# != - distinto de
# <= - Menor o igual
# >= - Mayor o igual
# and - AND lógico
# or - OR lógico
# not - NOT lógico


contador = 0

while contador < 10:
    print("While: " + str(contador))
    contador = contador + 1

for valor in range(0,100,3):
    print("For: " + str(valor))

for valor in "Cadena de texto":
    print(valor)


# 3 - Crea un programa que solicite dos valores enteros al usuario. Muestra por pantalla la tabla de multiplicar del primero hasta el segundo.
# Ejemplo: 5 10
# 5 x 5, 5 x 6, 5 x 7, 5 x 8, 5 x 9, 5 x 10

valor_1 = int(input("Introduce el primer valor: "))
valor_2 = int(input("Introduce el segundo valor: "))

for aux in range(valor_1,valor_2 + 1):
    resultado = valor_1 * aux
    print(str(valor_1) + " X " + str(aux) + " = " + str(resultado))


# 4 - Crea un programa que solicite una cadena de texto al usuario (como una contraseña). A continuación, vuelve a solicitar una cadena. Muestra si ambas coinciden o si son diferentes

cadena_1 = input("Introduce tu contraseña: ").lower()

cadena_2 = input("Vuelve a introducir tu contraseña: ").lower()

if cadena_1 == cadena_2:
    print("Son la misma")
else:
    print("Son distintas")

import math

# 5 - Crea un programa que permita al usuario introducir valores hasta que introduzca un valor negativo. Mostrar la media de todos los valores introducidos y el número de valores.

maximo = -math.inf
minimo = math.inf
suma_valores = 0
contador = 0
isTerminar = 0

while isTerminar == 0:
    valor = int(input("Introduce un valor (-1 para terminar): "))
    if valor < 0:
        isTerminar = 1
    else:
        suma_valores = suma_valores + valor
        contador = contador + 1
        if valor < minimo:
            minimo = valor
        if valor > maximo:
            maximo = valor

media = suma_valores / contador
print("La media es " + str(media))
print("El número de valores es " + str(contador))
print("El valor máximo es " + str(maximo))
print("El valor mínimo es " + str(minimo))


# 6 - Crea un programa que permita encontrar los números primos entre dos valores indicados por el usuario

valor_1 = int(input("Introduce el valor de inicio: "))
valor_2 = int(input("Introduce el valor de fin: "))

for v in range(valor_1, valor_2+1):
    contador = 2
    isPrimo = 0
    while contador < v and isPrimo == 0:
        resultado = v % contador
        if resultado == 0 and contador != resultado:
            isPrimo = 1
        contador = contador + 1
    if isPrimo == 0:
        print("El número " + str(v) + " es primo")

import random as rd

aleatorio = rd.randrange(0, 100)

print(aleatorio)


import sys

print(sys.argv)


import os

ruta = os.getcwd()

print(ruta)

#os.mkdir("/home/iago/Documentos/nuevo")

os.chmod("/home/iago/Documentos/nuevo",0o777)

os.chown("/home/iago/Documentos/nuevo",0,0)


import subprocess as sp

sp.run(["ls","/"])

sp.run(["mkdir","/home/iago/Documentos/otro"])

sp.run(["chmod","777","/home/iago/Documentos/otro"])

sp.run(["chown","root:root","/home/iago/Documentos/otro"])


import sys

argumentos = sys.argv
print(argumentos)


lista = [1,22,333,4444,55555,666666]

print("---Lista completa---")
print(lista)

print("---Acceso mediante índices---")
print(lista[3])

print("---Conocer tamaño de la lista---")
print(len(lista))

print("---Acceso parcial a la lista---")
print(lista[0:3])

print("---Modificación de valores por índice---")
lista[0] = 0
print(lista)

print("---Agregado de valores a la lista---")
lista.insert(0,1)
print(lista)

lista.insert(len(lista),7777777)
print(lista)

lista.append(88888888)
print(lista)

lista.extend([999999999,10101010101010101010])
print(lista)

print("---Eliminación de valores---")

lista.remove(333)
print(lista)

lista.pop()
print(lista)

lista.pop(4)
print(lista)

del lista[3]
print(lista)

#lista.clear()
#print(lista)

print("---Operaciones con listas---")
print("---Bucle por valores---")
for valor in lista:
    print(valor)

print("---Bucle con índices---")
for valor in range(len(lista)):
    print(lista[valor])


# 7 - Crea un programa que cree una lista de 10 elementos numéricos enteros al azar entre 0 y 100

import random as rd
lista = []
for v in range(0,10):
    azar = rd.randrange(0,101)
    lista.append(azar)

print("Lista completa")
print(lista)

# 8 - Crea un programa que contenga un lista de 10 valores numéricos enteros. Solicita al usuario un valor numérico. Si está en la lista, mostrar la posición en la que se encuentra. Si no se encuentra en la lista, informar de que no está en la lista.

lista = [1,2,3,4,5,6,7,8,9,10]

valor = int(input("Indica el valor que buscas: "))

if valor in lista:
    print(lista.index(valor))
else:
    print("No está en la lista")



isInLista = False
for v in lista:
    if v == valor:
        isInLista = True
        print(lista.index(v))

if not isInLista:
    print("El valor no se encuentra en la lista")

isInLista = False
for v in range(len(lista)):
    if lista[v] == valor:
        isInLista = True
        print(v)

if not isInLista:
    print("El valor no se encuentra en la lista")


# 9 - Crea un programa que solicite 10 valores numéricos enteros al usuario y los almacene en una lista. Ordena la lista de menor a mayor.

lista = []

contador = 0
while contador < 10:
    valor = int(input("Introduce un valor: "))
    lista.append(valor)
    contador = contador + 1

print("Lista completa:")
print(lista)
print("---Bubble sort---")
for i in range(len(lista)-1):
    print("Vuelta " + str(i))
    for j in range(len(lista)-i-1):
        if lista[j] > lista[j+1]:
            aux = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = aux
            print(lista)


lista.sort()


diccionario = {"clave":"valor","clave2":"valor2"}

# Muestra el diccionario completo
print(diccionario)

# Muestra un valor dada una clave
print(diccionario["clave"])

# Modifica el valor de una clave dada y lo muestra
diccionario["clave"] = "valorNuevo"
print(diccionario["clave"])


# Iterar por las claves
for key in diccionario:
    print(key)

# Iterar por los valores dada la clave
for key in diccionario:
    print(diccionario[key])

# Diccionario con valores de tipos de datos diversos
coches={"marca":"toyota",
        "modelo":"auris",
        "velocidadMax":200,
        "CV":90,
        "conductores":["Iago","Carlos","Ricardo"]}


# Declaración de función simple
def sumar_valores():
    entero_1 = 2
    entero_2 = 4
    resultado = entero_1 + entero_2
    print("Resultado: " + str(resultado))

sumar_valores()


#Declaración con valores de entrada

def sumar_valores(valor_1 = 5, valor_2 = 7, cadena = "Resultado: "):
    resultado = valor_1 + valor_2
    print("Resultado: " + str(resultado))

entero_1 = 2
entero_2 = 4

sumar_valores(entero_1, entero_2)
sumar_valores()


def sumar_valores(valor_1 = 5, valor_2 = 7):
    resultado = valor_1 + valor_2
    return resultado

entero_1 = 2
entero_2 = 4

suma = sumar_valores(entero_1, entero_2)

print("Resultado: " + str(suma))


class Coche:
    def __init__(self, marca="Citroen",modelo="C3"):
        self.m = marca
        self.mo = modelo

    def setMarca(self, marca):
        self.m = marca

    def getMarca(self):
        return self.m

coche_1 = Coche("Toyota", "Auris")
coche_2 = Coche()
print(coche_1.getMarca())
print(coche_2.getMarca())

trailer=[coche_1,coche_2]

for c in trailer:
    print(c.getMarca())


import requests as req

url = "https://ddragon.leagueoflegends.com/cdn/16.20.1/data/en_US/champion.json"

respuesta = req.get(url)

documento = respuesta.json()

campeones = documento["data"]

for k in campeones:
    print(k)


# Control de excepciones
try:
    print("hola")
except:
    print("Esto está mal")
finally:
    print("Esto sale siempre")







