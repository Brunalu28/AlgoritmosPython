r1 = float(input())
r2 = float(input())

area1 = 3.14*(r1**2)
area2 = 3.14*(r2**2)

if area1 > area2:
    print("Primeiro circulo")
elif area2 > area1:
    print("Segundo circulo")
else:
    print("Iguais")