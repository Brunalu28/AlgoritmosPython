n = list()
pos = list()
cont = 0

valor = int(input())
lista = list(map(int,input().split()))

lista2 = lista[:]
lista2.sort()

for i in range(len(lista2)):
    if lista[i] == lista2[i]:
        n.append(lista[i])
        pos.append(i+1)
        cont+=1
print(cont)
for i in range(cont):
    print(f"{n[i]} {pos[i]}")
