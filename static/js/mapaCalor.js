
//lista de colores
let colores = ['#FDEDEC','#FADBD8','#F5B7B1','#F1948A','#EC7063','#E74C3C','#CB4335','#B03A2E'];

let departamentos = ['lambA','piuA','tumA','apuA','aqpA','cusA','mddA','punA','moqA','tacA','ancA','cajA','huanA','libA','pasA','smartinA','ucayA','amazA','loretA','ayacA','callA','hcvA','icaA','junA','limaA'];
let depNombres = ['Lambayeque','Piura','Tumbes','Apurimac','Arequipa','Cusco','Madre de Dios','Puno','Moquegua','Tacna','Ancash','Cajamarca','Huanuco','La Libertad','Pasco','San Martín','Ucayali','Amazonas','Loreto','Ayacucho','Callao','Huancavelica','Ica','Junín','Lima']
let depIdsForPath = ['PER566','PER567','PER568','PER569','PER570','PER571','PER572','PER573','PER574','PER575','PER577','PER578','PER579','PER580','PER581','PER582','PER583','PER584','PER585','PER586','PER587','PER588','PER589','PER590','PER591'];
//Zona de 'a'

//variable para los tag a
var varForA;
var depIdPath;

for(var i=0; i<departamentos.length; i++){
    varForA = document.getElementById(departamentos[i]);
    varForA.setAttributeNS('http://www.w3.org/1999/xlink','title',depNombres[i]+'\nCasos:'+casosCant[i]);

    depIdPath = document.getElementById(depIdsForPath[i]);
    depIdPath.style.cssText = 'fill:' + asignarColor(casosCant[i]);
}


let CasosOrd;
CasosOrd = casosCant.slice();
CasosOrd.sort(function(a, b){return b - a});


let miTabla = "<table class='table'><thead class = 'thead-light'>";
miTabla += "<tr><th scope='col'>No.</th><th scope='col'>Departamento</th><th scope='col'>Cantidad de Casos</th></tr></thead>";
miTabla += "<tbody>";

for(var i=0; i<5; i++){
    miTabla += "<tr>";
    miTabla += "<th data-title='No.' scope='row'>"+(i+1)+"</th>";
    miTabla += "<th data-title='Departamento' scope='row'>"+ depNombres[asignarNombre(CasosOrd[i])] +"</th>";
    miTabla += "<th data-title='Cantidad de Casos' scope='row'>"+ CasosOrd[i] +"</th>";
    miTabla += "</tr>";
}

miTabla += "</tbody></table>";

document.getElementById('topFive').innerHTML = miTabla;

function asignarNombre(valor){
    for(var k=0; k<25; k++){
        if(casosCant[k] == valor) 
            return k;
    }
}

function asignarColor(casos){
    if(casos >= 0 && casos < 300) return colores[0];
    else if(casos >= 300 && casos < 600) return colores[1];
    else if(casos >= 600 && casos < 900) return colores[2];
    else if(casos >= 900 && casos < 1200) return colores[3];
    else if(casos >= 1200 && casos < 1500) return colores[4];
    else if(casos >= 1500 && casos < 1800) return colores[5];
    else if(casos >= 1800 && casos < 2100) return colores[6];
    else if(casos >= 2100 && casos <= 2400) return colores[7];
}