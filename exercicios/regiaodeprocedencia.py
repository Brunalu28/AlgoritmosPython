codigodeorigem = int(input())

sul = 5, 6, 7, 8, 9
sudeste = 10, 11, 12, 13, 14, 15

if codigodeorigem == 1:
    print("Nordeste")
elif codigodeorigem == 2:
    print("Norte")
elif codigodeorigem == 3 or codigodeorigem == 4:
    print("Centro-Oeste")
elif codigodeorigem in sul:
    print("Sul")
elif codigodeorigem in sudeste:
    print("Sudeste")