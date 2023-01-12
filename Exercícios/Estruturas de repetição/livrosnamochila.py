CAPACIDADE_MOCHILA = 18

cont = 0
total = 0

while True:
    livros = int(input())
    cont+= livros 
    if cont <= CAPACIDADE_MOCHILA:
        total += 1
    if cont > CAPACIDADE_MOCHILA:
        break
print(total)