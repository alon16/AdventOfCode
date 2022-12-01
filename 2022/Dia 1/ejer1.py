
with open("input.txt","r") as archivo:
    data=[]
    suma=0
    for linea in archivo:
        if(linea.strip()!=""):
            number=int(linea.strip())
            suma= suma + number
        else:
            data.append(suma)
            suma=0
    lista_ordenada=sorted(data, reverse=True)
    print(lista_ordenada[0])