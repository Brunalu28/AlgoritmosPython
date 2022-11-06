CAFEP = 10
CAFEG = 16
PROFESSORES = 7

total = 0


for i in range(PROFESSORES):
    quantcaixa = int(input())
    tamanho = input().lower()
    if quantcaixa > 0:
        if tamanho == "p":
             total += quantcaixa*CAFEP
        if tamanho == "g":
            total += quantcaixa*CAFEG
media = int((total*2)/7)
print(total)
print(media)