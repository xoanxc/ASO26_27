# 3 - Crea un programa que solicite dos valores al usuario. Muestra por pantalla la tabla de multiplicar del primero hasta el segundo.
# Ejemplo: 5 10
# 5x5, 5x6, 5x7, 5x8, 5x9, 5x10

valor_1 = int(input("Introduce el valor a multiplicar: "))
valor_2 = int(input("Introduce el valor límite: "))

for i in range(valor_1, valor_2 + 1):
    resultado = valor_1 * i
    print(str(valor_1) + " x " + str(i) + " = " + str(resultado))