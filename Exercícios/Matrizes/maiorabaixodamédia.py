
lista = []
listaresposta = []
cont = 0

while True:
    nomes = input()
    if nomes == "FIM":
        break
    else:
        notas = float(input())
        cont += notas
        lista.append([nomes, notas])
media = cont/len(lista)

for i in range(len(lista)):
    if lista[i][1] < media:
        listaresposta.append([lista[i][0], lista[i][1]])

if listaresposta == []:
    print("Ninguem abaixo da media")
else:
    ofc = []
    contmaiores = 0

    for i in range(len(listaresposta)):
        if listaresposta[i][1] > contmaiores:
            contmaiores = listaresposta[i][1]
    print("{:.1f}".format(contmaiores))
    for j in range(len(listaresposta)):
        if listaresposta[j][1] == contmaiores:
            print(listaresposta[j][0])
