altura = float(input())
raio = float(input())

volume = (3.14*raio**2)*altura
area1 = 3.14*raio**2
area2 = 2*3.14*raio*altura
areatotal = 2*area1 + area2

print("%.2f" % volume)
print("%.2f" % areatotal)