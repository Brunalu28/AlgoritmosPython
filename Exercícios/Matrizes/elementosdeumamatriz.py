matriz = []
juntar = ""
contprincipal = 0
contsecundaria = 0
contnegativos = 0
contpositivos = 0

ordem = input().split()

linha = int(ordem[0])
coluna = int(ordem[1])

# preenchendo a matriz

for i in range(linha):
    linhas = []
    for j in range(coluna):
        n1 = int(input())
        linhas.append(n1)
    matriz.append(linhas)

# imprimindo a matriz

print("Matriz formada:")

for k in range(len(matriz)):
    for x in range(len(matriz[k])):
        juntar += "{} ".format(matriz[k][x])
    print(juntar.strip())
    juntar = ""

# verificando se a matriz é quadrada

if linha == coluna:

    # calculando a diagonal principal da matriz

    for w in range(len(matriz)):
        for z in range(len(matriz[w])):
            if w == z:
                contprincipal += matriz[w][z]

    # calculando a diagonal secundaria da matriz

    matriz2 = matriz[::]
    matriz2.sort(reverse=True)

    for m in range(len(matriz2)):
        for a in range(len(matriz2[m])):
            if m == a:
                contsecundaria += matriz2[m][a]

    print("A diagonal principal e secundaria tem valor(es) {} e {} respectivamente.".format(contprincipal, contsecundaria))
    # verificando os valores negativos

    for y in range(len(matriz)):
        for p in range(len(matriz[y])):
            if matriz[y][p] < 0:
                contnegativos += 1
    print("A matriz possui {} numero(s) menor(es) que zero.".format(contnegativos))

    # verificando os valores positivos

    for q in range(len(matriz)):
        for r in range(len(matriz[q])):
            if matriz[q][r] > 0:
                contpositivos += 1
    print("A matriz possui {} numero(s) maior(es) que zero.".format(contpositivos))
    print()
else:
    print("A diagonal principal e secundaria nao pode ser obtida.")

    # verificando os valores negativos

    for y in range(len(matriz)):
        for p in range(len(matriz[y])):
            if matriz[y][p] < 0:
                contnegativos += 1
    print("A matriz possui {} numero(s) menor(es) que zero.".format(contnegativos))

    # verificando os valores positivos

    for q in range(len(matriz)):
        for r in range(len(matriz[q])):
            if matriz[q][r] > 0:
                contpositivos += 1
    print("A matriz possui {} numero(s) maior(es) que zero.".format(contpositivos))
