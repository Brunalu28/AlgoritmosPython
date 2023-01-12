lista1 = []
lista2 = []
cont = 0
valor1 = input().split()

numideias = int(valor1[0])
perfeita = int(valor1[1])

valor2 = [int(x) for x in input().split()]

for i in range(len(valor2)):
    for j in range(len(valor2)):
        if i != j:
            x = valor2[i] + valor2[j]
            if x == perfeita:
                cont+=1
if cont > 0:
    print("SIM")
else:
    print("NAO")