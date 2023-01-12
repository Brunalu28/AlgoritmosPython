notas = []
contmais = 0
contmenos =0

n = int(input())

for i in range(n):
    nota = int(input())
    notas.append(nota)
mediatotal = sum(notas)/n
for i in range(len(notas)):
    if notas[i] > mediatotal + (mediatotal*0.1):
        contmais+=1
    elif notas[i] < mediatotal - (mediatotal*0.1):
        contmenos+=1
print("{:.2f}".format(mediatotal))
print(contmais)
print(contmenos)