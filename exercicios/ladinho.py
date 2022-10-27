n = int(input())

lista = []
for i in range(n):
    lista.append(input())
for i in range(len(lista)):
    print("{:.3f}".format(float(lista[i])), end=" ")