ALIBABA = 83
ALCAPONE = 93
BRANCO = 0

votosalibaba = 0
votosalcapone = 0
votosbrancos = 0
votosnulos = 0

while True:
    votos = int(input())
    if votos == -1:
        break
    else:
        if votos == ALIBABA:
            votosalibaba+=1
        elif votos == ALCAPONE:
            votosalcapone+=1
        elif votos == BRANCO:
            votosbrancos+=1
        else:
            votosnulos+=1
prcalibaba = (votosalibaba*100)/(votosalibaba+votosalcapone+votosbrancos)
prcalcapone = (votosalcapone*100)/(votosalibaba+votosalcapone+votosbrancos)
print(votosalibaba)
print(votosalcapone)
print(votosbrancos)
print(votosnulos)
if votosalibaba > votosalcapone:
    print(ALIBABA)
else:
    print(ALCAPONE)
print("{:.2f}".format(prcalibaba))
print("{:.2f}".format(prcalcapone))