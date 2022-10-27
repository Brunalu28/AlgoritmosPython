CAIXADPREGO = 12
PRECO_CAIXA = 7.89

total = 7.89
pregos = 0

while True:
    quantpregos = int(input())
    pregos += quantpregos
    if quantpregos % 2 != 0:
        pregos -= quantpregos
        break
if pregos <= CAIXADPREGO:
    sobra = CAIXADPREGO - pregos
    print("{:.2f}".format(PRECO_CAIXA))
    print(sobra)
if pregos > CAIXADPREGO:
    while pregos > CAIXADPREGO:
        CAIXADPREGO += CAIXADPREGO
        PRECO_CAIXA += PRECO_CAIXA
        if pregos <= CAIXADPREGO:
            sobra = CAIXADPREGO - pregos
            print("{:.2f}".format(PRECO_CAIXA))
            print(sobra)
    
