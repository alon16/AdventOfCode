class CalculeIncreases:
    def main(self):
        increases=0
        anterior=0
        grupos= self.CreandoGrupos()
        for grupo in grupos:
            valorActual=grupo
            if(valorActual>anterior):
                increases+= 1
            anterior=valorActual
        print(increases-1)
    def CreandoGrupos(self):
        grupos=[]
        datos=[]
        with open("input.txt","r") as archivo:
            for linea in archivo:
                datos.append(int(linea.strip()))
            contador=0
            for linea in datos:
                contador+=1
                if(contador>=3):
                    grupos.append(datos[contador-2]+datos[contador-3]+linea)
        return grupos
main= CalculeIncreases()
main.main()