maiorvelocidade = 0
maiorano = 0
media = 0
cont = 0

while True:
    op = input().lower()
    if op == "n":
        if cont == 0:
            print("zero")
            break
        break
    else:
        ano = int(input())
        velocidade = float(input())
        cont += 1
        media += velocidade
        if ano > maiorano:
            maiorano = ano
        if velocidade > maiorvelocidade:
            maiorvelocidade = velocidade
if media > 0 and cont > 0:
    velocidademedia = media/cont
    print("{:.2f}".format(maiorvelocidade))
    print(maiorano)
    print("{:.2f}".format(media/cont))
