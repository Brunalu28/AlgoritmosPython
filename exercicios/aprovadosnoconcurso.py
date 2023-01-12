MIN_PORT = 40
MIN_MATH = 21
MIN_REDACAO = 7.0

cont = 0

while True:
    provaport = int(input())
    if provaport < 0:
        break
    else:
        provamath = int(input())
        redacao = float(input())
        if provaport >= MIN_PORT:
            if provamath >= MIN_MATH:
                if redacao >= MIN_REDACAO:
                    cont+=1
print(cont)
