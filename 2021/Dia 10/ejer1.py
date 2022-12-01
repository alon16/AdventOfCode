def main():
    result,unos,ceros=[],0,0
    with open("Dia10/input.txt","r") as archivo:
        for linea in archivo:
            list=[]
            list.extend(linea.strip())
            result.append(list)
        gamma=""
        elipson=""
    for x in range(12):
        for i in range(len(result)):
            if(int(result[i][x])== 1):
                unos+=1
            else: 
                ceros+=1
        if unos>ceros:
            gamma= gamma+"1"
        else:
            gamma= gamma+"0"
        unos=0
        ceros=0
    for item in gamma:
        if item == "1":
            elipson= elipson+"0"
        else :
            elipson= elipson+"1"
    print(int(gamma, 2)*int(elipson,2))
main()