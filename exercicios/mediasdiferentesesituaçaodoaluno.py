tipo = str(input())
if tipo != "a" and tipo != "h" and tipo != "p":
    print("Escolha um tipo de media valida.")
else:
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())

    if tipo == "p":
        p1 = int(input())
        p2 = int(input())
        p3 = int(input())
        media = ((n1*p1) + (n2*p2) + (n3*p3))/(p1+p2+p3)
    elif tipo == "h":
        media = 3/((1/n1) + (1/n2) + (1/n3))
    elif tipo == "a":
        media = (n1 + n2 + n3)/3
    print("%.2f" % media)
    if media >= 70 and media <= 100:
        print("Aprovado")
    elif media >= 40 and media < 70:
        print("Final")
    elif media >= 0 and media < 40:
        print("Reprovado")
    else:
        print("M�dia inv�lida")