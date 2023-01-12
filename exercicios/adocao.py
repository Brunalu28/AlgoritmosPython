idadeAdotante = int(input())
if idadeAdotante < 18:
    print("Não pode adotar")
else:
    ascendente = str(input())
    conjunta = str(input())
    unestavel = str(input())
    idadeAdotando = int(input())
    pdesconhecido = str(input())
    consentimentopais = str(input())
    consentimentoadotando = str(input())


    l1 = ascendente == "N"
    l2 = conjunta == unestavel
    l3 = (idadeAdotante - idadeAdotando) >= 16
    l4 = pdesconhecido == "N" and consentimentopais == "S"
    l5 = pdesconhecido == "S"
    responsaveis = l4 or l5
    l6 = (idadeAdotando >= 12 and consentimentoadotando == "S") or idadeAdotando < 12

    if l1 and l2 and l3 and responsaveis and l6:
        print("Pode adotar")
    else:
        print("Não pode adotar")