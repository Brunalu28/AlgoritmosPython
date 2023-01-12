k = int(input())
i = int(input())
m = int(input())
n = int(input())
d = int(input())

cont = 1
dragao = 0

while cont <= d:
    if cont%k == 0:
        dragao = dragao + 1
    elif cont%i == 0:
        dragao = dragao + 1
    elif cont%m == 0:
        dragao = dragao + 1
    elif cont%n == 0:
        dragao = dragao + 1
    cont = cont + 1
print(dragao)