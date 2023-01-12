arrecadado = 0
mesesfuturos = 0

valor_doacao = int(input())

while valor_doacao >= 1:
    op = int(input())
    while op != 1 and op != 2:
        print("Valor invalido")
        op = int(input())
    if op == 2:
        quantmeses = int(input())
        while quantmeses < 2 or quantmeses > 12:
            print("Favor digitar valor entre 2 e 12, inclusive")
            quantmeses = int(input())
        else:
            mesesfuturos += (quantmeses - 1)*valor_doacao
    arrecadado+= valor_doacao
    valor_doacao = int(input())
print("Total arrecadado para agora: R$ {:.2f}".format(arrecadado))
print("Total arrecadado para meses futuros: R$ {:.2f}".format(mesesfuturos))
