t1 = int(input())
t2 = int(input())
t3 = int(input())
t4 = int(input())

tomadas = (t1-1)+(t2-1) + (t3-1) + t4

if 2 <= t1 <= 6 and 2 <= t3 <= 6 and 2 <= t4 <= 6:
    print(tomadas)
else:
    print("Requisito violado")