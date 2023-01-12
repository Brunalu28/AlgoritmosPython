lista = []
lista2 = []
num = input().split()
competidores = int(num[0])
voltas = int(num[1])

for i in range(competidores):
    num2 = [int(x) for x in input().split()]
    lista.append(num2)
for j in range(len(lista)):
    comp = sum(lista[j])
    lista2.append(comp)
v = lista2.index(min(lista2))
print(v+1)

