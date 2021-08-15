var tempoEsgotado    = 300;
var tempoMenu = 200;
var fecharMenutimer = 0;
var itemMenu = 0;
var abrirMenu = 0;
var acaoMenu = false;
function func_abrirMenu()
{
	cancelarTempo();
	
	if($("a", this).html() == abrirMenu)
		return;
		
	if(acaoMenu)
		return;
		
	fecharMenu();

	if($("ul", this).size() == 0)
		return;
	
	acaoMenu = true;
	itemMenu = $(this).find('ul').fadeIn(tempoMenu, function() {acaoMenu = false;});
	abrirMenu = $("a", this).html();
	if (document.getElementById('ul'))
		document.getElementById('ul').className = 'current';
}

function fecharMenu()
{
	if(acaoMenu)
		return;
			
	if(itemMenu)
	{
		acaoMenu = true;
		itemMenu.fadeOut(tempoMenu, function() {acaoMenu = false;});
		itemMenu = null;
		abrirMenu = null;
	}
}

function func_tempoMenu()
{
	fecharMenutimer = window.setTimeout(fecharMenu, tempoEsgotado);
}

function cancelarTempo()
{
	if(fecharMenutimer)
	{
		window.clearTimeout(fecharMenutimer);
		fecharMenutimer = null;
	}
}

$(document).ready(function() {
	$('#menu > li').bind('mouseover', func_abrirMenu)
	$('#menu > li').bind('mouseout',  func_tempoMenu)
	$('#menu > li > ul').bind('mouseover',  cancelarTempo)
	$('#menu > li > ul > li').bind('mouseover',  cancelarTempo)
});

document.onclick = fecharMenu;