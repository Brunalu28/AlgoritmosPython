vogal = str(input())

if len(vogal) > 1:
    print("1 caractere, por favor!")
else:
    v = "aeiou"
    vM = "AEIOU"

    if vogal in v or vogal in vM:
        print("Eh vogal")
    else:
        print("Nao eh vogal")