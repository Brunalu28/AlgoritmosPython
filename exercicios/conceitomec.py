quantlivros = int(input())
quantalunos = int(input())

conceito = (quantalunos/quantlivros)

if conceito <= 8:
    print("A")
elif conceito >= 9 and conceito <=12:
    print("B")
elif conceito >=13 and conceito <=18:
    print("C")
elif conceito > 18:
    print("D")