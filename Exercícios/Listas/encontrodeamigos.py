lista = []
x = 0
n = int(input())

p = [int(x) for x in input().split()]

for i in range(1,max(p)):
    for j in range(len(p)):
        if p[j] >= i:
            a = p[j]-i
            x += a
        elif p[j] <= i:
            a = i - p[j]
            x +=a
    lista.append(x)
    x = 0
d = lista.index(min(lista))
print("{} {}".format(min(lista),d+1))