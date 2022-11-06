nome = str(input())
curso = str(input())
periodo = int(input())
trabalhou = str(input())
cre = int(input())
recomendacao = int(input())
monitor = ""
pontos = 0
potosantigos =0
while nome != "sair":
    pontos = 0
    if curso == "EC" and periodo >= 3:
        if trabalhou == "sim":
            pontos += 50
        pontos = pontos + cre + (recomendacao * 10)
        if pontos > potosantigos:
            monitor = nome
            potosantigos = pontos
    elif curso == "TEL" and periodo >= 2:
        if trabalhou == "sim":
            pontos += 50
        pontos = pontos + cre + (recomendacao * 10)
        if pontos > potosantigos:
            monitor = nome
            potosantigos = pontos
    nome = str(input())
    if nome == "sair":
        break
    curso = str(input())
    periodo = int(input())
    trabalhou = str(input())
    cre = int(input())
    recomendacao = int(input())
print("O bolsista serah:", monitor)
