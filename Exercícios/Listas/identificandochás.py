cont = 0

valor = int(input())
lista = list(map(int,input().split()))

for i in range(len(lista)):
    if valor == lista[i]:
        cont+=1
print(cont)