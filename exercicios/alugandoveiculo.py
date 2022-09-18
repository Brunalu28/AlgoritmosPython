diaria = int(input())
quilometragem = int(input())

valordadiaria = (diaria*90)
extra = quilometragem - diaria * 100

if extra <= 0:
    print("%.2f" % valordadiaria)
elif extra > 0:
   valortotal = (extra*12) +valordadiaria
   print("%.2f" % valortotal)