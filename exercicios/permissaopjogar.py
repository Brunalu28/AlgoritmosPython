idadejogador = int(input())
tipodejogo = str(input())

if idadejogador < 0 or idadejogador > 130:
    print("Idade invalida.")
elif idadejogador >= 21 and tipodejogo == "azar":
    print("Pode entrar!")
elif idadejogador < 21 and tipodejogo == "azar":
    print("Volte daqui há alguns anos.")
elif idadejogador >= 14 and tipodejogo == "mmorpg":
    print("Pode entrar!")
elif idadejogador < 14 and tipodejogo == "mmorpg":
    print("Volte daqui há alguns anos.")
elif idadejogador >= 10 and tipodejogo == "moba":
    print("Pode entrar!")
elif idadejogador < 10 and tipodejogo == "moba":
    print("Volte daqui há alguns anos.")
elif tipodejogo == "casual":
    print("Pode entrar!")
else:
    print("Jogo invalido.")