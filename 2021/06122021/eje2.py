import input
peces= input.firtspeces()
posicion=[]
def main():
        for dia in range(256):
            calcular(peces)
            for i in posicion:
                peces[i]=6
                peces.append(8)
            print(str(dia)+" "+str(len(peces)))
        print(len(peces))
def calcular(peces):
    posicion.clear()
    for index in range(len(peces)):
        if(peces[index]==0):
            posicion.append(index)
        peces[index]-=1
    return peces
main()