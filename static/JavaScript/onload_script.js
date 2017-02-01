$(function () {
	getForm();
	$(".search-content").keyup( function ()
	{
		$(".search-results").html("");
		if(this.value.length > 3)
		{
			$(".content-box").css({display:"none"});
			$('.banner-image').css({display:"none"});
			$(".search-box").css({margin:"50px auto auto 0px"});
			$.get("http://conquering.com:8000/search",{q:this.value},function(data)
			{
				$.each(data, function(index, value)
				{
					console.log(value);
					$(".search-results").append(
					`
						<div class = 'search-response'>
							<div class = 'col-xs-2'>
								Title:
							</div>
							<a class = 'col-xs-10' href = 'http://conquering.com:8000/Articles/`+value.uri+`'>
							`
							+ value.title +
							`
							</a>
							<blockquote>
								<p>
								`
								+ value.summary +
								`
								</p>
								<a href = 'http://conquering.com:8000/Articles/`+value.uri+`'>Read More</a>
								<footer>Posted Date: <cite>` + value.timestamp.substring(0,10) + `</cite>
								</footer>
							</blockquote>
						</div>
					`
					);
				});
			})
		}
		if(this.value.length <= 3)
		{
			$(".content-box").css({display:"block"});
			$('.banner-image').css({display:"block"});
		}

	});
	$(".glyphicon-info-sign").click(function()
	{
		var info_box = $(".zip-code-info");
		var _display = info_box[0].style.display;
		if(_display == "" || _display == "none")
			info_box.css({display:"block"});
		else
			info_box.css({display:"none"});
	});
});

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

function getForm()
{
	var hash = window.location.hash;
	switch(hash)
	{
		case "#register":
			$(".register-box").css({display:"block"});
			$(".log-in-box").css({display:"none"});
			break;
		case "#recover":
			$(".recover-box").css({display:"block"});
			$(".log-in-box").css({display:"none"});
			break;
		default:
			$(".register-box").css({display:"none"});
			$(".log-in-box").css({display:"block"});
			$(".recover-box").css({display:"none"});
			break;
	}
}



