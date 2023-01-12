gabarito = [str(x) for x in input()]

nomeacima = ""
acima = 0
nota = 0
listanotas = []
listanotasenomes = []

while True:
    nome = input()
    if nome == "sair":
        break
    else:
        resposta = [str(x) for x in input()]
        for i in range(len(gabarito)):
            if resposta[i] == gabarito[i]:
                nota+=20
        listanotas.append(nota)
        listanotasenomes.append([nota, nome])
        nota = 0
media = sum(listanotas)/len(listanotas)

for j in range(len(listanotas)):
    if listanotas[j] > media:
        acima+=1
print(acima)
for k in range(len(listanotasenomes)):
    if listanotasenomes[k][0] >= acima:
        acima = listanotasenomes[k][0]
        nomeacima = listanotasenomes[k][1]
print(nomeacima)
