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
"""""

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


