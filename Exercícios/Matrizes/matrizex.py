turma = [[5.0, 4.5, 7.0, 5.2, 6.1], [2.1, 6.5, 8.0, 7.0, 6.7], [8.6, 7.0, 9.1, 8.7, 9.3]]

juntar = ""
# string que vai imprimir os valores sem os colchetes

for i in range(len(turma)):
    # for que vai ser executado 3 vezes, pois diz respeito ao tamanho da lista "turma"
    for j in range(len(turma[i])):
        #  for que vai ser executado 5 vezes, pois é referente aos valores que estão em cada uma das listas
        juntar += "{:.1f} ".format(turma[i][j])
        # junção dos valores formatados e um ao lado do outro
    print(juntar.strip())
    # impressão dos valores sem espaços no inicio e fim
    juntar = ""
    # string de junção esvaziada para receber os valores referentes a proxima linha da matriz