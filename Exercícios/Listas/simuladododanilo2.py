cont = 1
lista = []
n = int(input())

pontos = [int(x) for x in input().split()]
p1 = pontos[0]

for i in range(1,len(pontos)):
    if p1 == pontos[i]:
        cont+=1
    else:
        cont = 1
    lista.append(cont)
    p1 = pontos[i]
print(max(lista))