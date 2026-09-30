# 6 - Crea un programa que permita encontrar los números primos entre dos valores indicandos por el usuario.

valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))

for i in range(valor1, valor2 + 1):
    contador = 2
    while contador < i:
        resultado = i % contador
        if resultado == 0 and contador != resultado;


