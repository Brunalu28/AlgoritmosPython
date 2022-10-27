PACOTE = 5
PRECO_MINUTO = 0.5
DESCONTO = 0.2

cont = 0
soma = 5

while True:
    minutos = input()
    cont += 1
    if minutos == "*":
        break
    else:
        if cont > 5:
            minutos = float(minutos)
            minutoamais = (minutos*PRECO_MINUTO)
            soma += minutoamais
if soma > 50:
    desconto = (soma*DESCONTO)
    total= soma - desconto
    print("{:.2f}".format(total))
else:
    print("{:.2f}".format(soma))