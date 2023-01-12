n = int(input())

cont = 0

while n != -1:
    for i in range(2,n):
        if n % i == 0:
            cont+=1
    if cont == 0 and n >=2:
        print(1)
    else:
        print(0)
    n = int(input())