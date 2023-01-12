matriz = []
cont = 0
juntar = "tr(A) = "
ordem = int(input())

# forma de fazer sem usar matriz

for i in range(ordem):
    n = [float(x) for x in input().split()]
    if i+1 == ordem:
        cont += n[i]
        juntar += "({:.2f}) = {:.2f}".format(n[i], cont)
    else:
        juntar += "({:.2f}) + ".format(n[i])
        cont += n[i]
print(juntar)

# forma de fazer usando matriz

for i in range(ordem):
    n = [float(x) for x in input().split()]
    matriz.append(n)
for j in range(ordem):
    if j+1 == ordem:
        cont += matriz[j][j]
        juntar += "({:.2f}) = {:.2f}".format(matriz[j][j], cont)
    else:
        cont += matriz[j][j]
        juntar += "({:.2f}) + ".format(matriz[j][j])
print(juntar)