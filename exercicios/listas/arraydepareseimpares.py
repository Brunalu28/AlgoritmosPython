pares = []
impares = []

for i in range(1, 16):
    v = int(input())
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(pares)