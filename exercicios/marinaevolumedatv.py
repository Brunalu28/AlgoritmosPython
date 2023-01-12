VMAX = 100
VMIN = 0

valor_final = 0

while True:
    volumetv_inicial = int(input())
    valordastrocas = int(input())
    if volumetv_inicial >= 0 and volumetv_inicial <= 100 and valordastrocas >= 0 and valordastrocas <= 10:
                for i in range(1, valordastrocas+1):
                    volume = int(input())
                    if volumetv_inicial <= 100 and volumetv_inicial >= 0:
                        if volume > 0 and volume < 100:
                            valor_final = volumetv_inicial + volume
                            volumetv_inicial = valor_final
                        if volumetv_inicial > 100:
                            volumetv_inicial = valor_final = 100
                    if volumetv_inicial >= 0 and volumetv_inicial <= 100:
                        if volume < 0:
                            valor_final = valor_final + volume
                            volumetv_inicial = valor_final
                            if volumetv_inicial < 0:
                                volumetv_inicial = valor_final = 0
                print(valor_final)
                break
