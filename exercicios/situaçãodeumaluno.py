n1 = int(input())
n2 = int(input())
n3 = int(input())

media = float((n1 + n2 + n3)/3)

if media >= 70 and media <= 100:
    print("A media do aluno foi", "%.2f" % media, "e ele foi APROVADO")
elif media < 40 and media >= 0:
    print("A media do aluno foi", "%.2f" % media, "e ele foi REPROVADO")
elif media >= 40 and media <= 70:
    print("A media do aluno foi", "%.2f" % media, "e ele foi FINAL")
else: 
    print("Media invalida")