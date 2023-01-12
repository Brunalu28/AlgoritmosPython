dias = float(input())
km = float(input())

aluguemdesc = ((30*dias)+(km*0.01))-(((30*dias)+(km*0.01))*10)/100

print("%.2f" % aluguemdesc)
