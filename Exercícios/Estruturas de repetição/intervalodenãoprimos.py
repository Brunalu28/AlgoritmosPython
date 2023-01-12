n = int(input())
print(1, end=" ")
if n != 0:
    for i in range(1,n+1):
        m1 = i % 2 
        m2 = i % 3
        m3 = i % 5
        m4 = i % 7
        if m1 == 0 or m2 == 0 or m3 == 0 or m4 == 0:
            if i == 2 or i == 3 or i == 5 or i == 7:
                i+=1
            else:
                print(i, end=" ")
                i +=1
        else:
            i += 1