n = 1

while n >= 0 and n <= 12:
    fatorial = 1
    n = int(input())
    if n != -1:
        while n > 1:
            fatorial*=n
            n-=1
        print(fatorial)

