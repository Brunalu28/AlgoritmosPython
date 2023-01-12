n1 = int(input())
while n1 > 9 or n1 < 1:
    print("Insira um número inicial entre 1 e 9")
    n1 = int(input())
n2 = int(input())
while n2 > 9 or n2 < 1:
    print("Insira um número final entre 1 e 9")
    n2 = int(input())

if n2 < n1:
    print("Nenhuma tabuada nesse intervalo")
else:
    for i in range(n1,n2+1):
        for x in range(1, 10):
            print("{} x {} = {}".format(i, x, i*x))
        print("")
