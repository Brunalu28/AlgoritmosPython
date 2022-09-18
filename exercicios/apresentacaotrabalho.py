req1_intgraf = int(input("Trabalho aborda Interface Grafica? (0 - Nao 1 - Sim)\n"))
req2_intart = int(input("Trabalho aborda Inteligencia Artificial? (0 - Nao 1 - Sim)\n"))
req3_encaps = int(input("Trabalho aborda Encapsulamento? (0 - Nao 1 - Sim)\n"))
req4_ident = int(input("Trabalho aborda Indentacao? (0 - Nao 1 - Sim)\n"))
req5_stru = int(input("Trabalho aborda Structs? (0 - Nao 1 - Sim)\n"))

if req1_intgraf == 1 or req2_intart == 1:
    if req3_encaps == 1 and req4_ident == 1:
        if req5_stru == 1:
            print("Seu trabalho sera avaliado.")
        else:
            print("Seu trabalho nao sera avaliado, nota 0.")
    else:
            print("Seu trabalho nao sera avaliado, nota 0.")
else:
    print("Seu trabalho nao sera avaliado, nota 0.")
