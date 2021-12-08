depth,forward,aim=0
with open("input.txt","r") as archivo:
    for linea in archivo:
        x= linea.split(' ')
        if x[0] == "up":
            aim-= int(x[1])
        elif x[0] == "down":
            aim+= int(x[1])
        else:
            forward+= int(x[1])
            depth+= aim*int(x[1])
print(forward*depth)