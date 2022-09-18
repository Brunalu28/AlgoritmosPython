n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 > n2 and n1 > n3 and n2 > n3:
    print(n1, n2, n3, sep="\n")
    
elif n2 > n1 and n2 > n3 and n1 > n3:
    print(n2, n1, n3, sep="\n")
    
elif n3 > n1 and n3 > n2 and n2 > n1:
    print(n3, n2, n1, sep="\n")
    
elif n1 > n2 and n1 > n3 and n3 > n2:
    print(n1, n2, n3, sep="\n")
    
elif n2 > n1 and n2 > n3 and n3 > n1:
    print(n2, n3, n1, sep="\n")
    
elif n3 > n2 and n3 > n1 and n1 > n2:
    print(n3, n1, n2, sep="\n")
