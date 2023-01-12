crime_delator = str(input())

oproubo = "roubo"
optrafico = "tráfico"
ophomicidio = "homicídio"

if crime_delator != oproubo and crime_delator != optrafico and crime_delator != ophomicidio:
    print("Crime inválido.")
else:
    if crime_delator == oproubo or crime_delator == optrafico:
        valorcrime_delator = int(input())
    if  crime_delator == oproubo or crime_delator == optrafico or crime_delator == ophomicidio:
        crimedelatado = str(input())
    if crimedelatado != oproubo and crimedelatado != optrafico and crimedelatado != ophomicidio:
        print("Crime inválido.")
    if crimedelatado == oproubo or crimedelatado == optrafico:
        valorcrime_delatado = int(input())
    if crime_delator == oproubo or crime_delator == optrafico:
        if crimedelatado == ophomicidio:
            print("Delação concedida.")
    if crime_delator == oproubo and crimedelatado == optrafico:
        if valorcrime_delatado > (valorcrime_delator*3):
            print("Delação concedida.")
        else:
            print("Delação rejeitada.")
    if crime_delator == ophomicidio:
        if crimedelatado == ophomicidio:
            print("Delação concedida.")
        if crimedelatado == optrafico or crimedelatado == oproubo:
            print("Delação rejeitada.")
    if crime_delator == oproubo and crimedelatado == oproubo:
        if valorcrime_delatado > (5*valorcrime_delator):
            print("Delação concedida.")
        else:
            print("Delação rejeitada.")
    if crime_delator == optrafico and crimedelatado == optrafico:
        if valorcrime_delatado > (5*valorcrime_delator):
            print("Delação concedida.")
        else:
            print("Delação rejeitada.")
