psnr = int(input())
enquadramento =str(input())
exposicao = str(input())

enquadramento_bom = enquadramento == "bom" or enquadramento == "excelente"

if psnr >= 80 and psnr <=90:
    if  enquadramento_bom and exposicao == "bem exposta":
        print("para imprimir")
    elif enquadramento_bom and exposicao == "superexposta" or exposicao == "subexposta":
        print("boa")
    else:
        print("marromeno")
elif psnr >= 50 and psnr < 80:
    if enquadramento == "excelente" and exposicao == "bem exposta":
        print("boa")
    else:
        print("marromeno")
elif psnr < 50:
    if enquadramento == "excelente" and exposicao == "bem exposta":
        print("marromeno")
    else:
        print("lixo")