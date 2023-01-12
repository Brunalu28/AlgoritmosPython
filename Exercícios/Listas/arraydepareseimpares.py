pares = []
impares = []



for i in range(1, 16):
    v = int(input())
    if v % 2 != 0:
        impares.append(v)
        if len(impares) >= 5:
            for j in range(5):
                print("impar[{}] = {}".format(j, impares[j]))
            impares.clear()
    else:
        pares.append(v)
        if len(pares) >= 5:
            for k in range(5):
                print("par[{}] = {}".format(k, pares[k]))
            pares.clear()
    if i == 15 and len(impares) != 0 and len(pares) != 0:
        for k in range(len(impares)):
            print("impar[{}] = {}".format(k, impares[k]))
        for m in range(len(pares)):
            print("par[{}] = {}".format(m, pares[m]))



