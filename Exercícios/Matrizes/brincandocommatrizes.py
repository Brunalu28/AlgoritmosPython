soma = 0
cont = -1000
matriz = []
diagp = 0
for i in range(3):
    linhas = []
    for j in range(3):
        valores = int(input())
        if j == i:
            diagp += valores
        soma += valores
        if valores > cont:
            cont = valores
        linhas.append(valores)
    matriz.append(linhas)
if cont > 0:
    delta = 1
elif cont == 0:
    delta =  0
else:
    delta = -1
print("{:.2f} {} {} {}".format((soma/9), cont, delta, diagp))
