maiorvalor = 0
quempagoumais = ""
cont = 0

total = float(input())
nsindicalistas = int(input())

if nsindicalistas == 0:
    print("Nao ha conta ou funcionario suficiente para pagar a conta")
else:
    for i in range(1, nsindicalistas + 1):
        nome = input()
        valorpago = float(input())
        cont += valorpago
        if valorpago <= total:
            if valorpago >= maiorvalor:
                quempagoumais = nome
                maiorvalor = valorpago
    print("{} pagou R$ {:.1f}".format(quempagoumais, maiorvalor))
    mediatotal = cont
    if mediatotal > total:
        excedente = mediatotal - total
        print("Valor excedente: sobra R$  {:.1f}".format(excedente))
    else:
        falta = total - mediatotal
        print("Valor insuficiente: falta R$  {:.1f}".format(falta))