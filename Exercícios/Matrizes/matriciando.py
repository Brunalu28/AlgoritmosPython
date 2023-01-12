diagprincipal = 0
try:
    n1 = int(input())
    n2 = int(input())
except ValueError:
    print("erro")
else:
    if n1 != n2 or n1 < 0 or n2 < 0:
        print("erro")
    else:
        matriz = []
        for i in range(n1):
            linhas = []
            for j in range(n2):
                valores = int(input())
                linhas.append(valores)
                if i == j:
                    if valores > 0:
                        diagprincipal += valores
            matriz.append(linhas)

        maiores_linhas = []

        for i in range(len(matriz)):
            contmaioreslinhas = -1000
            for j in range(len(matriz[i])):
                if matriz[i][j] > contmaioreslinhas:
                    contmaioreslinhas = matriz[i][j]
            maiores_linhas.append(contmaioreslinhas)

        print(maiores_linhas)

        maiores_colunas = []

        for i in range(len(matriz)):
            contmaiorescolunas = -1000
            for j in range(len(matriz[i])):
                if matriz[j][i] > contmaiorescolunas:
                    contmaiorescolunas = matriz[j][i]
            maiores_colunas.append(contmaiorescolunas)

        print(maiores_colunas)

        contotal = -1000
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] > contotal:
                    contotal = matriz[i][j]

        print(contotal)

        print(diagprincipal)

        diff = 0


        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if i + j == n1 - 1 and i == 0:
                    diff = matriz[i][j]
                elif i + j == n1 - 1:
                    diff -= matriz[i][j]
        print(diff)