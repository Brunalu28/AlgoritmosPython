n = int(input("Digite um número: "))
print("""Escolha uma das bases:
      [1] - binário
      [2] - Octal
      [3] - hexadecimal""")
op = int(input("Digite sua opção: "))
if op != 1 and op != 2 and op != 3:
    print("Opção inválida")
else:
    if op == 1:
        print("{} convertido para binário é igual a {}".format(n, bin(n)[2:]))
    elif op == 2:
        print("{} convertido para octal é igual a {}".format(n, oct(n)[2:]))
    elif op == 3:
        print("{} convertido para hexadecimal é igual a {}".format(n, hex(n)[2:]))