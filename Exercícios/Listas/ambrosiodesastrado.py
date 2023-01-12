lista = []
juntar = ""

quant = int(input())

for i in range(quant):
    n = input().split()
    num = int(n[0])
    letra = n[1]
    lista.append([num, letra])
lista.sort()

for j in range(quant):
    juntar += lista[j][1]
print(juntar)