valor1 = float(input())
dias = 6
valor_poupado = valor1
cont = 0

while dias > 0:
    valor = float(input())
    valor_poupado = valor_poupado + valor
    if valor - valor1 >= 0.5:
        cont+=1
    valor1 = valor
    dias = dias - 1
print("R$", "%.2f" % valor_poupado)
print(cont)