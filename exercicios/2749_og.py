filhos = input().split()

while filhos[0] != "0" and filhos[1] != "0":
    meninos = int(filhos[0])
    meninas = int(filhos[1])
    soma = meninos + meninas
    print(soma)
    filhos = input().split()