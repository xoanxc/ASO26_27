import random

# 7 - Crea un programa que cree una lista de 10 elementos numéricos enteros al azar entre 0 y 100

lista = []
for valor in range(10):
    lista.append(random.randrange(0,101))

print(lista)
