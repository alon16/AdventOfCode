anterior=0
increases=0
with open("input.txt","r") as archivo:
    for linea in archivo:
        valorActual=int(linea.strip())
        if(valorActual>anterior):
            increases+= 1
        anterior=valorActual
print(increases-1)