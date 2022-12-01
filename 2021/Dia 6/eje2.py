import input
peces= input.firtspeces()
# peces=[3,4,3,1,2]
posicion=[]
def main():
        diasSinPasar= 80
        maximo=max(peces)
        tam= len(peces)
        tam
        resto= 0
        dia=0
        # for i in range(80):
        #     if( i% 8 == 0):
        #         tam= tam*2
        #     else:
        #         resto= dia %8
        # print(tam)
        while  dia <= 80:
            if(dia== maximo):
                tam=tam*2
                dia=0
                maximo=maximo+8
            dia+=1
        print( tam+resto)
        #     calcular(peces)
        #     for i in posicion:
        #         peces[i]=6
        #         peces.append(8)
        #     print(str(dia)+" "+str(len(peces)))
        # print(len(peces))
def calcular(peces):
    posicion.clear()
    for index in range(len(peces)):
        if(peces[index]==0):
            posicion.append(index)
        peces[index]-=1
    return peces
main()