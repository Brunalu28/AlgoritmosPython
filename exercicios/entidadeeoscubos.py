# c = 1
# i = 1
# quantcubos = int(input())

# andares = c + (i + 1) + (i + 2)

# while quantcubos > 1:



soma = 0
i = 0
n = int(input())

while True:
    soma += (i + 1) + (i + 2)
    i+=1
    if soma >= n:
        print(i)
        break

