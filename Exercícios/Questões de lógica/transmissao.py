tvvideo = float(input())
taudio = float(input())
tdados = float(input())
capacidade = float(input())

qdmax = ((tvvideo*5.2) + (taudio*3.4) + (tdados*1.5))/capacidade

print("%.2f" % qdmax)
