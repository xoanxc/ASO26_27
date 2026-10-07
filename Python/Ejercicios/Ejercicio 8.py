# 8 - Crea un programa que contenga una lista de 10 valores númericos enteros. Solicita al usuario un valor numérico. Si está en la lista, mostrrar la posición en la que se encuentra. Si no se encuentra en la lista, informar de que no está en la lista.

lista = [1,2,3,4,5,6,7,8,9,10]

valor = int(input("Indica el valor que buscas:"))
isInLista = False
for i in lista:
    if i == valor:
        isInLista = True
        print(lista.index(i))
if not isInLista:
    print("El valor no se encuentra en la lista")