tipodefigura = str(input())

if tipodefigura == "Q":
    lado = float(input())
    areaquad = (lado*lado)
    perimetroquad = (lado*4)
    print("%.2f" % areaquad, "%.2f" % perimetroquad, sep="\n")
elif tipodefigura == "R":
    largura = float(input())
    altura = float(input())
    arearet = (largura*altura)
    perimetroret = 2*(largura+altura)
    print("%.2f" % arearet, "%.2f" % perimetroret, sep="\n")
elif tipodefigura == "C":
    raio = float(input())
    areacir = 3.14*(raio**2)
    circunferencia = 2*3.14*raio
    print("%.2f" % areacir, "%.2f" % circunferencia, sep="\n")
else:
    print("Nenhuma figura selecionada")

