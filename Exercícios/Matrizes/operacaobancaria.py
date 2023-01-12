cont_creditos = 0
cont_debitos = 0
contlinhas = -1
matriz = []

while True:
    valores = [float(x) for x in  input().split()]
    contlinhas+=1
    if valores[0] == -1 or contlinhas > 100:
        break
    else:
        matriz.append(valores)
for i in range(len(matriz)):
    if matriz[i][0] == 0.0:
        cont_debitos += matriz[i][1]
    else:
        cont_creditos += matriz[i][1]

saldo = cont_creditos - cont_debitos

print("Creditos: R$ {:.2f}".format(cont_creditos))
print("Debitos: R$ {:.2f}".format(cont_debitos))
print("Saldo: R$ {:.2f}".format(saldo))
