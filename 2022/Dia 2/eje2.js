
var fs = require('fs');
var input=fs.readFileSync(process.cwd()+'/2022/Dia 2/input.txt').toString().split("\n");
const EMPATE=3;const PERDIDO=0;const GANADO=6;
const totales = input.map((element, index) => {
        var ronda=0;
        if(element.includes("Y")){
            ronda=EMPATE+elegido(element[0],"EMPATE" );
        }
        else if(element.includes("Z")){
            ronda=GANADO+elegido(element[0],"GANADO" );
        }
        else if(element.includes("X")){
            ronda= PERDIDO+elegido(element[0],"PERDIDO" )
        }
        return ronda
    });
    var total=totales.reduce((a, b) => a + b, 0);
    console.log(total);
function elegido(elemento, result){
    switch(result){
        case "EMPATE":
            if (elemento=="A")
            return 1
            else if(elemento=="B")
            return 2
            else elemento==("C")
            return 3
        case "GANADO":
            if (elemento=="A")
                return 2
            else if(elemento=="B")
                return 3
            else elemento==("C")
                return 1
        case "PERDIDO":
            if (elemento=="A")
                return 3
            else if(elemento=="B")
                return 1
            else elemento==("C")
                return 2
        }
}