time = str(input())

gsw = "GSW"
hou = "HOU"
cle = "CLE"
bos = "BOS"

if time != gsw and time != hou and time != cle and time != bos:
    print("Nenhum time de interesse jogando.")
else:
    nomejogador = str(input())
    arremessotentado2p = int(input())
    arremessoconvertido2p = int(input())
    arremessotentado3p = int(input())
    arremessoconvertido3p = int(input())

    pontostotais = arremessoconvertido2p + (0.5*arremessoconvertido3p)/(arremessotentado2p+arremessotentado3p)
    percentual2p = arremessoconvertido2p/arremessotentado2p
    percentual3p = arremessoconvertido3p/arremessotentado3p

    if pontostotais >= 30 or percentual2p >= 0.5 and arremessotentado2p >= 10 or percentual3p >= 0.4 and arremessotentado3p >= 7 or percentual2p == 1 or percentual3p == 1:
        print("O time", time, "estah jogando, e", nomejogador, "estah indo bem.")
    else:
        print("O time", time, "estah jogando, mas", nomejogador, "nao estah indo bem.")

