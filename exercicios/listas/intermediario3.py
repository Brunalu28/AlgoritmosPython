lista = []

for i in range(3):
    n = int(input())
    lista.append(n)

lista.remove(max(lista))
lista.remove(min(lista))


print(lista[0])