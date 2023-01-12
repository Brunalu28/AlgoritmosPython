n = int(input())

for i in range(n):
    palavra = input().lower()
    p = palavra.replace(" ","")
    inv = p[::-1]
    if p == inv:
        print("SIM")
    else:
        print("NAO")
