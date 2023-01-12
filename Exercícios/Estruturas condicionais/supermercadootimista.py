diadasemana = str(input())
precodoproduto = float(input())
opdoproduto = str(input())
nomedoproduto = str(input())

diadametade = "seg", "ter", "qua"
diaumterco = "qui", "sex"
diatriplo = "sab"

precometade = (precodoproduto/2)
precoterco = (precodoproduto/3)
precotriplo = (precodoproduto*3)
precodobro = (precodoproduto*2)

if diadasemana in diadametade and opdoproduto == "ouro":
    print("O preco do produto", nomedoproduto, "no dia", diadasemana, "eh", "%.2f" % precometade)
elif diadasemana in diaumterco and precodoproduto > 10 and precodoproduto < 100:
    print("O preco do produto", nomedoproduto, "no dia", diadasemana, "eh", "%.2f" % precoterco)
elif diadasemana in diatriplo and opdoproduto == "prata":
    print("O preco do produto", nomedoproduto, "no dia", diadasemana, "eh", "%.2f" % precotriplo)
else:
    print("O preco do produto", nomedoproduto, "no dia", diadasemana, "eh", "%.2f" % precodobro)


