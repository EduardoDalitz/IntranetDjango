jQuery.browser = {};
(function () {
jQuery.browser.msie = false;
jQuery.browser.version = 0;
if (navigator.userAgent.match(/MSIE ([0-9]+)\./)) {
jQuery.browser.msie = true;
jQuery.browser.version = RegExp.$1;
}
})();


$(document).ready(function(){

    console.log("funcionou!");

    var deletar = $('.delete-btn');
    var procurarBotao = $('#search-btn');
    var procurarFormulario = $('#search-form');
    
    $(deletar).on('click', function(e){

        e.preventDefault();

        var deletar = $(this).attr('href');
        var resultado = confirm('Deletar?')

        if (resultado) {
            window.location.href = deletar;
        }
    });

    $(procurarBotao).on('click', function(){
        procurarFormulario.submit();
    })

});