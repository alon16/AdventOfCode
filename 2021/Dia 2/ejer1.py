depth=0
forward=0
with open("02122021/input.txt","r") as archivo:
    for linea in archivo:
        x= linea.split(' ')
        if x[0] == "up":
            depth-= int(x[1])
        elif x[0] == "down":
            depth+= int(x[1])
        else:
            forward+= int(x[1])
print(forward*depth)