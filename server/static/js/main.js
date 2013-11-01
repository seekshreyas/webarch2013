var MADLIB = MADLIB || {};

MADLIB = (function(){

	// regex reference link:
	// http://blog.mattheworiordan.com/post/13174566389/url-regular-expression-for-links-with-or-without-the

	var re = '/((([A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+|(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w-_]*)?\??(?:[-\+=&;%@.\w_]*)#?(?:[.\!\/\\w]*))?)/'


	var init = function(){
		console.log("page loaded");

		// parseLyrics();
		evtHandler();
	};


	//Event Handler
	function evtHandler(){
		jQuery('#madlib-input').submit(function(event){
			event.preventDefault();

			lurl = jQuery('#field-long').val();

			console.log(lurl);
			


		});
	}





	return {
		'init' : init
	};
})();


jQuery(document).ready(function(){
	MADLIB.init();
});