$(window).on("hashchange", function(){
	if(location.hash.slice(1)=="register"){
		$(".card").addClass("extend");
		$("#login").removeClass("selected");
		$("#register").addClass("selected");
	} else {
		$(".card").removeClass("extend");
		$("#login").addClass("selected");
		$("#register").removeClass("selected");
	}
});
$(window).trigger("hashchange");


$(document).ready(function () {
	$('input').each(function () {
	  $(this).on('focus', function () {
		$(this).parent('.wrapper').addClass('active');
	  });
	  $(this).on('blur', function () {
		if ($(this).val().length === 0) {
		  $(this).parent('.wrapper').removeClass('active');
		}
	  });
	  if ($(this).val() !== '') $(this).parent('.wrapper').addClass('active');
	});
  });