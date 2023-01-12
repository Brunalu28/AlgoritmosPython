n = int(input())

if n < 0:
    print(n)
else:
    while n >= 0:
        print(n)
        n = int(input())
        if n < 0:
            print(n)