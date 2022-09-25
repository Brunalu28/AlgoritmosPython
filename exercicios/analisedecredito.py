salario = float(input())
rendacomp = float(input())

limite = (salario*0.30)

if rendacomp<limite:
    valorapagar = limite - rendacomp
    print("%.2f" % valorapagar)
elif rendacomp>limite:
    print("0.00")