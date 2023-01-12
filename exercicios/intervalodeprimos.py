a = int(input())
b = int(input())

if a > b:
    for i in range (a, b-1, -1):
        eh_primo = True
        for x in range(2,i):
            if i % x == 0:
                eh_primo = False
                break
        if eh_primo and i != 1:
            print(i)
else:
    for i in range (b, a-1, -1):
        eh_primo = True
        for y in range(2,i):
            if i % y == 0:
                eh_primo = False
                break
        if eh_primo and i != 1:
            print(i)