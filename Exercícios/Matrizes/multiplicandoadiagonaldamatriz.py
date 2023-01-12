while True:
    n = int(input())
    if n == 0:
        break
    else:
        matriz = []
        for i in range(4):
            linhas = []
            for p in range(4):
                valores = int(input())
                linhas.append(valores)
            matriz.append(linhas)

    for j in range(len(matriz)):
        for k in range(len(matriz[j])):
            if j == k:
                mult = matriz[j][k]*n
                matriz[j][k] = mult


    for x in range(len(matriz)):
        for m in range(len(matriz[x])):
            print("{}".format(matriz[m][x]), end=" ")
        print()
