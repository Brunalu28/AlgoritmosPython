total = float(input())
funcionarios = int(input())

quempagoumais = ""
pagoumais = 0
quempagoumenos = ""
pagoumenos = 0
arrecadado = 0


for i in range(1, funcionarios+1):
    nomef = input()
    valorf = float(input())
    arrecadado += valorf
    if valorf == 0:
        quempagoumenos = nomef
        pagoumenos = valorf
        if pagoumenos == pagoumais:
            quempagoumais = nomef
            pagoumais = valorf
    elif valorf >= pagoumais:
            quempagoumais = nomef
            pagoumais = valorf
    elif valorf <= ultimopagamento:
            quempagoumenos = nomef
            pagoumenos = valorf
    ultimopagamento = valorf
print("Conta: R$ {:.2f}".format(total))
print("Arrecadado: R$ {:.2f}".format(arrecadado))
if arrecadado == total:
    print("Foi arrecadado exatamente o valor da conta.")
elif arrecadado > total:
    print("{} pagou R$ {:.2f}".format(quempagoumais, pagoumais))
    sobra = arrecadado - total
    print("Valor excedente: sobra R$ {:.2f} a ser devolvido a {}".format(sobra, quempagoumais))
else:
    print("{} pagou R$ {:.2f}".format(quempagoumais, pagoumais))
    falta = total - arrecadado
    print("Valor insuficiente: falta R$ {:.2f}".format(falta))
    print("{} pagou R$ {:.2f} e precisa pagar mais R$ {:.2f}".format(quempagoumenos, pagoumenos, falta))