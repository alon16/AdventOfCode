import input
peces= input.firtspeces()
posicion=[]
def main():
    for dia in range(80):
        calcular(peces)
        for i in posicion:
            peces[i]=6
            peces.append(8)
    print(len(peces))
def calcular(peces):
    posicion.clear()
    for index in range(len(peces)):
        if(peces[index]==0):
            posicion.append(index)
    decrementar(peces)
def decrementar(peces):
    for item in range(len(peces)):
        peces[item]-=1
    return peces
main()