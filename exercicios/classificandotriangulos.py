triangulo = input().split()

while triangulo[0] != "FIM":
    a = int(triangulo[0])
    b = int(triangulo[1])
    c = int(triangulo[2])
    equilatero = a == b and b == c and c == a
    isosceles = a == b or b == c or c == a
    escaleno = a != b and b != c and c != a
    triangulo_valido = (a + b > c) and (a + c > b) and (c + b > a)
    if equilatero and triangulo_valido:
        print("EQUILATERO")
    elif isosceles and triangulo_valido:
        print("ISOSCELES")
    elif escaleno and triangulo_valido:
        print("ESCALENO")
    else:
        print("INVALIDO")
    triangulo = input().split()
