valor = int(input())
lista = list(map(int,input().split()))
print("Menor valor:", min(lista))
print("Posicao:", lista.index(min(lista)))