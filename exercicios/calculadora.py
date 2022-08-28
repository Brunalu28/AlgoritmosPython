## Calculadora em Python ##

print("CALCULADORA EM PYTHON")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

S = n1 + n2 
D = n1 / n2
M = n1*n2
SB = n1 - n2

print("Soma (S)")
print("Divisão (D)")
print("Multplicação (M)")
print("Subtração (SB)")

Menu = S, SB, D, M

if Menu == S:
  print(S)

if Menu == D:
  print(D)

if Menu == SB:
  print(SB)

if Menu == M:
  print(M)
