matrizA = []
matrizB = []
matrizC = []
total1 = 0

valores = [int(x) for x in input().split()]

for i in range(valores[0]):
    valoresA = [int(x) for x in input().split()]
    matrizA.append(valoresA)

for j in range(valores[1]):
    valoresB = [int(x) for x in input().split()]
    matrizB.append(valoresB)

linhasC = []
for i in range(len(matrizA)):
    for j in range(len(matrizB)):
        total1 += (matrizA[0][j] * matrizB[j][i])
    linhasC.append(total1)
    total1 = 0
matrizC.append(linhasC)

linhasC = []
for i in range(len(matrizA)):
    for j in range(len(matrizB)):
        total1 += (matrizA[1][j] * matrizB[j][i])
    linhasC.append(total1)
    total1 = 0
matrizC.append(linhasC)

juntar = ""
for i in range(len(matrizC)):
    for j in range(len(matrizC[i])):
        juntar += "{} ".format(matrizC[i][j])
    print(juntar.strip())
    juntar = ""

