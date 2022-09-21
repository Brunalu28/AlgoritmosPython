vingador = str(input())
v1 = "Homem de Ferro"
v2 = "Hulk"
v3 = "Capit�o Am�rica"
v4 = "Thor"
v5 = "Gavi�o Arqueiro"
v6 = "Vi�va Negra"
if vingador != v1 and vingador != v2 and vingador != v3 and vingador != v4 and vingador != v5 and vingador != v6:
    print("Vingador Inv�lido")
else:
    poder = str(input())
    energia = int(input())

    poderv1 = "Armadura de Ferro"
    poderv2 = "For�a Bruta"
    poderv3 = "Escudo"
    poderv4 = "Martelo"
    poderv5 = "Arco e Flecha"
    poderv6 = "Intelig�ncia"

    energiav1 = 10
    energiav2 = 5
    energiav3 = 7
    energiav4 = 4
    energiav5 = 12
    energiav6 = 20

    if vingador == v1:
            if poder == poderv1:
                if energia >= energiav1:
                    print(v1, "conseguiu derrotar Thanos")
                else:
                    print(v1, "NAO conseguiu derrotar Thanos, chamem outro Vingador")
            elif poder == poderv2:
                print(v1, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v2)
            elif poder == poderv3:
                print(v1, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v3)
            elif poder == poderv4:
                print(v1, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v4)
            elif poder == poderv5:
                print(v1, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v5)
            elif poder == poderv6:
                print(v1, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v6)
    elif vingador == v2:
            if poder == poderv2:
                if energia >= energiav2:
                    print(v2, "conseguiu derrotar Thanos")
                else:
                    print(v2, "NAO conseguiu derrotar Thanos, chamem outro Vingador")
            elif poder == poderv1:
                print(v2, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v1)
            elif poder == poderv3:
                print(v2, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v3)
            elif poder == poderv4:
                print(v2, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v4)
            elif poder == poderv5:
                print(v2, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v5)
            elif poder == poderv6:
                print(v2, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v6)
    elif vingador == v3:
            if poder == poderv3:
                if energia >= energiav3:
                    print(v3, "conseguiu derrotar Thanos")
                else:
                    print(v3, "NAO conseguiu derrotar Thanos, chamem outro Vingador")
            elif poder == poderv2:
                print(v3, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v2)
            elif poder == poderv1:
                print(v3, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v1)
            elif poder == poderv4:
                print(v3, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v4)
            elif poder == poderv5:
                print(v3, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v5)
            elif poder == poderv6:
                print(v3, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v6)
    elif vingador == v4:
            if poder == poderv4:
                if energia >= energiav4:
                    print(v4, "conseguiu derrotar Thanos")
                else:
                    print(v4, "NAO conseguiu derrotar Thanos, chamem outro Vingador")
            elif poder == poderv2:
                print(v4, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v2)
            elif poder == poderv3:
                print(v4, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v3)
            elif poder == poderv1:
                print(v4, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v1)
            elif poder == poderv5:
                print(v4, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v5)
            elif poder == poderv6:
                print(v4, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v6)
    elif vingador == v5:
            if poder == poderv5:
                if energia >= energiav5:
                    print(v5, "conseguiu derrotar Thanos")
                else:
                    print(v5, "NAO conseguiu derrotar Thanos, chamem outro Vingador")
            elif poder == poderv2:
                print(v5, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v2)
            elif poder == poderv3:
                print(v5, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v3)
            elif poder == poderv4:
                print(v5, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v4)
            elif poder == poderv1:
                print(v5, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v1)
            elif poder == poderv6:
                print(v5, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v6)
    elif vingador == v6:
            if poder == poderv6:
                if energia >= energiav6:
                    print(v6, "conseguiu derrotar Thanos")
                else:
                    print(v6, "NAO conseguiu derrotar Thanos, chamem outro Vingador")
            elif poder == poderv2:
                print(v6, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v2)
            elif poder == poderv3:
                print(v6, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v3)
            elif poder == poderv4:
                print(v6, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v4)
            elif poder == poderv5:
                print(v6, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v5)
            elif poder == poderv1:
                print(v6, "NAO conseguiu derrotar Thanos")
                print("Esse � o poder do", v1)
