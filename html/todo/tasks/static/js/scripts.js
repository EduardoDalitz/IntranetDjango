
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

    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    
    $(deleteBtn).on('click', function(e){

        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Deletar?')

        if (result) {
            window.location.href = delLink;
        }
    });

    $(searchBtn).on('click', function(){
        searchForm.submit();
    })

});