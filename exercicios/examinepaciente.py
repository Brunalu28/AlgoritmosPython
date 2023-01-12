temperatura = float(input())
std = str(input())

if temperatura >= 37 and std == "S":
    print("Exames Especiais")
elif temperatura >= 37 and std =="N":
    print("Exames Basicos")
elif temperatura < 37 and std == "S":
    print("Exames Basicos")
elif temperatura < 37 and std == "N":
    print("Liberado")
else:
    print("Erro")