competidores = int(input())
pontosminimos = int(input())

cont = 0
vencedores = 0

for i in range(competidores):
    faseum = int(input())
    fasedois = int(input())
    if faseum == 0 or fasedois == 0:
        vencedores += 0
    else:
        cont += faseum
        cont+= fasedois
        if cont >= pontosminimos:
            vencedores += 1
        if cont < pontosminimos:
            vencedores += 0
    cont = 0
print("{}".format(vencedores))
