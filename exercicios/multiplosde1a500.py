soma = 0
cont = 0
for i in range(1,500):
    if i % 2 != 0:
        if i % 3 == 0:
            cont +=1
            soma+=i
            i-=1
print("A soma dos multiplos de 1 a 500 é {}, possuindo um total de {} elementos.".format(soma, cont))