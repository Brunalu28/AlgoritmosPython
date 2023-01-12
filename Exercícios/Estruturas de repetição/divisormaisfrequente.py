d = int(input())

cont = 0

for i in range(d, 1, -1):
    if d % i == 0:
        cont+=i