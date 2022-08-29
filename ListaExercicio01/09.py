x = int(input("Número de entrada: "))

lista = []
lista.append(0)
lista.append(1)

for number in range(2, 9 + x):
    lista.append(lista[number - 1] + lista[number - 2])

print(lista[x - 1:])