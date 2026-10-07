# 9 - Crea un programa que solicite 10 valores numéricos enteros al usuario y los almacene en una lista, Ordena la lista de menor a mayor.

lista = []

for i in range(10):
    valor = int(input(f"Introduce el número entero {i + 1} de 10: "))
    lista.append(valor)

lista.sort()

print("Lista ordenada de menor a mayor:", lista)
