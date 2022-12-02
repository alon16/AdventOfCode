
var fs = require('fs');
var input=fs.readFileSync(process.cwd()+'/2022/Dia 2/input.txt').toString().split("\n");
const EMPATE=3;const PERDIDO=0;const GANADO=6;

const totales = input.map((element, index) => {
        var ronda=0;
        if(element.includes("A") && element.includes("X")||
        element.includes("B") && element.includes("Y") ||
        element.includes("C") && element.includes("Z")){
            ronda=EMPATE;
        }
        else if(element.includes("A") && element.includes("Y")||
        element.includes("B") && element.includes("Z") ||
        element.includes("C") && element.includes("X")){
            ronda=GANADO;
        }
        else ronda= PERDIDO;

        if(element.includes("X"))
        ronda= ronda+1
        else if(element.includes("Y"))
        ronda= ronda+2
        else if(element.includes("Z"))
        ronda= ronda+3
        return ronda
    });
    var total=totales.reduce((a, b) => a + b, 0);
    console.log(total);