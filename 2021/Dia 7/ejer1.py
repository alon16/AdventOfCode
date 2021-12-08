import input
posicion= input.posiciones()
combustible=[]
def main():
    for i in posicion:
        aux=0
        for x in range(len(posicion)):
            consumo=i-posicion[x]
            if(consumo>0):
                aux+=consumo;
            else:
                aux-=consumo;
        combustible.append(aux)
    minimo=min(combustible)
    print(minimo)
main()
            

