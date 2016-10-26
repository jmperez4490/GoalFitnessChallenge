// $(function () {
	
// });

window.onscroll = function()
{
	var y_screen = window.pageYOffset;
	if(y_screen >= 50)
	{
		$("nav").css({"background-color":"#CFCFCF",opacity:".7","z-index":"3"});
	}
	if(y_screen < 50)
	{
		$("nav").attr('style','');
	}
};