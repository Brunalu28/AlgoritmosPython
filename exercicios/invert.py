nome = input()

junt =""
tamanho = len(nome)

for i in range(tamanho-1, -1, -1):
    junt+= nome[i]
print(junt)