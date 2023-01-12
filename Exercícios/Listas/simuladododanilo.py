lista = []
nlinhas = int(input())
frases = ""

for i in range(nlinhas):
    frase = [str(x) for x in input().split()]
    ajuste = (frase[0]).capitalize()
    frase[0] = ajuste
    for j in range(len(frase)):
        if "." in frase[j]:
            if j+1 < len(frase):
                ajuste2 = (frase[j+1]).capitalize()
                frase[j+1] = ajuste2
    lista.append(frase)
for k in range(len(lista)):
    for h in range(len(lista[k])):
        frases += "{} ".format(lista[k][h])
    print(frases.strip())
    frases = ""