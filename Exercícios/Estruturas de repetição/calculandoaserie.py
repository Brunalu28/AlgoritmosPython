n = int(input())

soma = 0
s = " "
for i in range(1, n + 1):
    serie = i / (i*3)
    soma += serie
    s += f'{i}/{i*3}'
    if i < n :
        s += " + "
print(s)
print("{:.2f}".format(soma))