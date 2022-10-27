n1 = int(input())

i = 1

while n1 > i * (i + 1) * (i + 2):
    i += 1
    if n1 == i * (i + 1) * (i + 2):
        print(i,"*", i + 1,"*", i + 2, "=", n1)
        print("Verdadeiro")
if n1 != i * (i + 1) * (i + 2):
    print("Falso")