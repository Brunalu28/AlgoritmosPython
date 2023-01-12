turma = []
# total de alunos
for i in range(3):
    linhas = []
    # criando lista que se refere aos alunos da turma (3)
    # vai ser importante pra zerar a lista no proximo loop
    for j in range(5):
        notas = float(input())
        linhas.append(notas)
    # as notas foram adicionadas a linha, uma nota seguida a outra
    turma.append(linhas)
    # por fim, toda a linha é inserida na matriz turma, que depois pode ser impressa com um for

# imprimindo a matriz pra verificar se tá tudo ok

juntar = ""

for k in range(len(turma)):
    for x in range(len(turma[k])):
        juntar += "{:.1f} ".format(turma[k][x])
    print(juntar.strip())
    juntar = ""
