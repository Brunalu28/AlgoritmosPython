a = int(input())
b = int(input())

if a >=b:
    for i in range (a-1, b, -1):
        print("{}".format(i))