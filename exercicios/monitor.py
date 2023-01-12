minimo = 0
max = 100
media = 70

maior_media = 0

while True:
    media_aluno = int(input())
    if media_aluno == 0:
        break
    else:
        if media_aluno > minimo and media_aluno <= max:
            nome = input()
            horas = int(input())

            if horas >= 8 and media_aluno >= media:
                while True:
                     cre = int(input())
                     if cre >= minimo and cre <= max:
                         while True:
                            notadeprova = int(input())
                            if notadeprova >= minimo and notadeprova <= max:
                                if notadeprova < media:
                                    print("Aluno reprovado na prova de monitoria!")
                                    break
                                else:
                                    mediafinal = (media_aluno*0.4) + (cre*0.1)+ (notadeprova*0.5)
                                    if mediafinal >= media:
                                        print("Aluno aprovado! Sua media foi {:.2f}.".format(mediafinal))
                                        if mediafinal > maior_media:
                                            maior_media = mediafinal
                                            monitoraprov = nome
                                        break
                                    else:
                                        print("Aluno reprovado na selecao. Media= {:.2f}.".format(mediafinal))
                                        break
                         break
            else:
                print('Aluno NAO pode concorrer.')
                pass
        else:
            pass
if maior_media != 0:
    print('Resultado da monitoria: {}, {:.2f}.'.format(monitoraprov, maior_media))
else:
    print('Resultado da monitoria: Sem alunos aprovados.')
