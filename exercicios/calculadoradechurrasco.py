opcarnes = str(input())

completo = "C"
boiefrango = "BF"
boiesuino = "BS"

if opcarnes != completo and opcarnes != boiefrango and opcarnes != boiesuino:
    print("Opção inválida.")
else:
    paodealho = str(input())
    bebidapadulto = str(input())
    bebidapcrianca = str(input())
    quantcrianca = int(input())
    quantadulto = int(input())

    bebidaspadulto_consumir = ((2*quantadulto)*8)
    bebidaspcrianca_consumir = ((0.5*quantcrianca)*6)

    if opcarnes == completo:
        bovina_valor = ((0.2 * quantadulto) * 32) + ((0.2 * quantcrianca) * 32)
        frango_valor = (0.1 * quantadulto) * 18
        porco_valor = (0.1 * quantadulto) * 15
        valor_total = bovina_valor + frango_valor + porco_valor
    elif opcarnes == boiefrango:
        bovina_valor = ((0.25 * quantadulto) * 32) + ((0.2 * quantcrianca) * 32)
        frango_valor = (0.15 * quantadulto) * 18
        valor_total = bovina_valor + frango_valor
    else:
        bovina_valor = ((0.25 * quantadulto) * 32) + ((0.2 * quantcrianca) * 32)
        porco_valor = (0.15 * quantadulto) * 15
        valor_total = bovina_valor + porco_valor
    if bebidapadulto == "S":
        valor_total = valor_total + bebidaspadulto_consumir
    if bebidapcrianca == "S":
        valor_total = valor_total + bebidaspcrianca_consumir
    if paodealho == "N":
        valor_total = valor_total - (valor_total*0.02)
    print("R$:", "%.2f" % valor_total)
