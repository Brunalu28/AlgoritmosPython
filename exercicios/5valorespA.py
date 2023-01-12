cont = 0
for i in range(1, 5+1):
    a = float(input("Digite um valor:\n"))
    if a < 0:
        cont+= 1
print("Forma digitados {} numeros negativos". format(cont))