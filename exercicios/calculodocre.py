semestre = int(input())

if semestre < 0 or semestre > 10:
    print("entrada invalida")
else:
    ch = int(input())
    nota = int(input())
    situadisc = str(input())

    somadenotas = 0
    somadech = 0

    while semestre > 0 and semestre <= 10:
        if not situadisc in ["AE", "DT", "AD", "DD", "DE", "DC"] and ch in [33, 50, 67, 83]:
            cre = (nota*ch)
            somadenotas = somadenotas + cre
            somadech = somadech + ch
        semestre = int(input())
        if semestre > 0 and semestre <= 10:
            ch = int(input())
            nota = int(input())
            situadisc = str(input())
    if somadenotas != 0 and somadech != 0 and cre != 0:
        cretotal = somadenotas/somadech
        print("%.2f" % cretotal)
    else:
        print("entrada invalida")