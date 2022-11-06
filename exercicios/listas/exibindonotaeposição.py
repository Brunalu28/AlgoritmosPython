lista = []
soma = 0
n = int(input())
if n == 0:
    print("Numero de notas invalido.")
else:
    for i in range(1, n+1):
        notas = float(input())
        lista.append(notas)
        soma
        print("Nota {}: {:.1f}".format(i, notas))
    media = sum(lista)/n
    print("Media: {:.2f}".format(media))