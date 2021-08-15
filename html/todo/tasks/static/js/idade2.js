function idade(ano_ani, mes_ani, dia_ani){
    var d = new Date,
    ano_atual = d.getFullYear(),
    mes_atual = d.getMonth() + 1,
    dia_atual = d.getDate(),
    
    
    qnts_anos = ano_atual - ano_ani;

    if (mes_atual < mes_ani || mes_atual == mes_ani && dia_atual <dia_ani) {
        qnts_anos--;
    }
    return qnts_anos < 0 ? 0: qnts_anos;
}



var d = new Date,
ano_atual = d.getFullYear(),
mes_atual = d.getMonth() + 1,
dia_atual = d.getDate(),

hora    = d.getHours();          
min     = d.getMinutes();        
seg     = d.getSeconds();        

str_hora = hora + ':' + min + ':' + seg;

anos = (dia_atual) + '/' + (mes_atual)+ '/'+ ano_atual ;
console.log(str_hora+  ' -- '+ anos);
idade_brascola = idade(1953,09,25) 
console.log(idade_brascola);
document.write(idade_brascola)

