ano = input().split()

ni = int(ano[0])
nf = int(ano[1])

cont = 0

for i in range(ni, nf+1):
    if i  % 4 == 0 and i % 400 == 0:
        print(i)
        cont+=1
    elif i % 4 == 0 and i % 100 != 0:
        print(i)
        cont+=1
if cont == 0:
    print(-1)