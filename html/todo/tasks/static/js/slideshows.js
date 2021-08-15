function apresentarBanner() {
    var $ativa = $('#slideshow DIV.active');

    if ( $ativa.length == 0 ) $ativa = $('#slideshow DIV:last');

    var $next =  $ativa.next().length ? $ativa.next()
        : $('#slideshow DIV:first');

    $ativa.addClass('last-active');

    $next.css({opacity: 0.0})
        .addClass('active')
        .animate({opacity: 1.0}, 600, function() {
            $ativa.removeClass('active last-active');
        });
}

$(function() {
    setInterval( "apresentarBanner()", 5000 );
});