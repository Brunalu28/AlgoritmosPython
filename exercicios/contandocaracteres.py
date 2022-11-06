cont = 0
maiorp = ""

while True:
    frase = input().split()
    if frase[0] == "0":
        break
    else:
        for i in range(len(frase)):
            t = len(frase[i])
            if (i + 1) == len(frase):
                print(t)
            else:
                print(t, end="-")
            if t >= cont:
                maiorp = frase[i]
                cont = t
print('Maior palavra:'.format(maiorp))
