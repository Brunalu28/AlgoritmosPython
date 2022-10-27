n = int(input())
while n != 0:
    n1 = 0
    n2 = 1
    n3 = 0
    y = ""
    for i in range(0,n):
        y += str(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        if i < n -1:
            y += " "
    print(y)
    n = int(input())