
var fs = require('fs');
var input=fs.readFileSync(process.cwd()+'/2022/Dia 5/input1.txt').toString().split("\n");

var movimientos=fs.readFileSync(process.cwd()+'/2022/Dia 5/input2.txt').toString().split("\n");
var almacen=[];
input.forEach(element=>almacen.push(Array.from(element)));
for(i=0;i<movimientos.length;i++){
    var movida=movimientos[i].match(/(\d+)/g);
    mover=parseInt(movida[0]); desde=parseInt(movida[1])-1; hacia=parseInt(movida[2])-1;
    for(j=mover; j>0; j--){
        current=j-1;
        if(almacen[desde].length!=0){
            cantDesde=almacen[desde].length-1
            var grupo=almacen[desde].splice(cantDesde-current,1);
            almacen[hacia]=almacen[hacia].concat(grupo);
        }
    }
}
var orden="";
almacen.forEach(element=>{
    var lastOne= element.length -1 ;
orden+=element[lastOne]
});
console.log(orden);