passeio = input().lower()

pessoas = 1
cine = 0
bolich = 0

while pessoas <= 6:
    if passeio == "cinema":
        cine+=1
    elif passeio == "boliche":
        bolich+=1
    passeio = input().lower()
    pessoas = pessoas +1
if cine > bolich:
    print("CINEMA")
else:
    print("BOLICHE")