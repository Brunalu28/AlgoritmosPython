listanotas1 = []
listanotas = []
notasenomes = []
distancia = []
j1 = ""
j2 = ""

for i in range(5):
    nota = float(input())
    listanotas.append(nota)
    listanotas1.append(nota)
    nome = input()
    notasenomes.append([nota, nome])
listanotas1.sort(reverse=True)
for j in range(len(listanotas1)):
    j1 += "{:.2f} ".format(listanotas1[j])
print(j1.strip())
media = sum(listanotas)/len(listanotas)
print("{:.2f}".format(media))
for k in range(len(listanotas)):
    if media >= listanotas[k]:
        dif = media - listanotas[k]
    else:
        dif = listanotas[k] - media
    distancia.append(dif)
    j2 += "{:.2f} ".format(dif)
print(j2.strip())
d = distancia.index(max(distancia))
print(notasenomes[d][1].capitalize())
print(d)

