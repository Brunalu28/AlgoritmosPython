n = int(input())
esq = " "
for i in range(1, n+1):
    esq += str(i)
    if i <= n:
        esq += " "
    print(esq.strip())
