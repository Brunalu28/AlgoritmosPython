soma = 0
cont = 0
matriz = []
diagp = 0
v = 0
for i in range(3):
    linhas = []
    for j in range(3):
        valores = int(input())
        v += 1
        if j != i:
            diagp += valores
        if valores > 0:
            soma += valores
        else:
            v -= 1
        if i == 0 and j == 0:
            cont = valores
        else:
            if valores < cont:
                cont = valores
        linhas.append(valores)
    matriz.append(linhas)
if cont % 2 == 0:
    delta = 1
else:
    delta = 0
print("{:.2f} {} {} {}".format((soma/v), cont, delta, diagp))
