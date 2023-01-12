import math
temp = float(input())
massa = float(input())

vmg = (3*8.31*temp)/massa

vmg2 = math.sqrt(vmg)

print("%.2f" % vmg2)
