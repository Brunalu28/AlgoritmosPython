n1 = float(input())
n2 = float(input())
n3 = float(input())

p1 = int(input())
p2 = int(input())
p3 = int(input())

a = (n1 + n2 + n3)/3

p = ((n1*p1) + (n2*p2) + (n3*p3))/(p1+p2+p3)

h = 3/((1/n1) + (1/n2) + (1/n3))

print("a:", "%.1f" % a)
print("p:", "%.1f" % p)
print("h:", "%.1f" % h)