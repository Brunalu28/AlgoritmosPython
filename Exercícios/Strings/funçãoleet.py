def leet(str):
    str1 = str.replace(" ", "")
    teste = (str1).isalpha()
    if teste == False:
        print("numeros")
        print("0")
    elif str == "":
        print("numeros")
        print("0")
    else:
        listaletras = ["a", "e", "i", "o", "t", "s"]
        listasimbolos = ["@", "3", "1", "0","7", "5"]
        inverso = str[::-1]

        nova = ""
        cont = 0
        for i in range(len(inverso)):
            for j in range(len(listaletras)):
                if inverso[i] == listaletras[j]:
                    nova += listasimbolos[j]
                    cont+= 1
                    break
            if inverso[i] not in listaletras:
                nova += inverso[i]
        print(nova)
        print(cont)

frase = input().lower()
leet(frase)