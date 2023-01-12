n = int(input())

d1 = 1
d2 = 4
soma = 0
s = ""
serie = 0

for i in range(1, n + 1):
    if i % 2 != 0: # Verifica se o valor é impar
        serie = d1 / d2
        soma += serie
        s += f'{d1}/{d2}'
        d1 += 2
        d2 +=4
    if i % 2 == 0: # Verifica se o valor é par
        serie += 1
        soma+= 1
        s += f'{1}'
    if i < n:
        s += " + "
print("{:.2f}".format(soma))
print(s)

