tipodeataque = str(input())
tipodepokemon = str(input())


if tipodeataque == tipodepokemon:
    print("Empate")
if tipodeataque == "Fogo" and tipodepokemon == "Planta":
    print("Vantagem")
elif tipodeataque == "Agua" and tipodepokemon == "Fogo":
    print("Vantagem")
elif tipodeataque == "Planta" and tipodepokemon == "Agua":
    print("Vantagem")
if tipodeataque == "Fogo" and tipodepokemon == "Agua":
    print("Desvantagem")
elif tipodeataque == "Agua" and tipodepokemon == "Planta":
    print("Desvantagem")
elif tipodeataque == "Planta" and tipodepokemon == "Fogo":
    print("Desvantagem")
