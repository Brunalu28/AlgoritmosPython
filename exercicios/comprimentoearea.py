raio = float(input())
angulo = float(input())


comparco = 2*3.14*raio*(angulo/360)

areasetor = 3.14*(raio**2)*angulo/360


print("%.2f" % comparco,"%.2f" % areasetor, sep="\n")