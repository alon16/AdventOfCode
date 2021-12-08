import input
posicion= input.posiciones()
combustible=[]
def main():
    posicion.sort()
    for i in range(max(posicion)):
        aux=0
        for x in range(len(posicion)):
            consumo=0
            pasos=posicion[x]-i
            if(pasos<0):
                pasos=abs(pasos)
            for dato in range(pasos):
                consumo+= dato+1
            aux+= consumo
        combustible.append(aux)
    minimo=min(combustible)
    print(minimo)
main()
            

