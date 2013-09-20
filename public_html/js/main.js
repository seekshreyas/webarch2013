var MADLIB = MADLIB || {};

MADLIB = (function(){


	var init = function(){
		console.log("page loaded");
		parseLyrics();
	};


	function parseLyrics(){
		//to show prettier lyrics
		//I love this song. it deserves proper respect of being 
		//displayed right :)
		jQuery('#wrapper-madlib p').each(function(){

			var lyric = jQuery(this).text();

			newlyric = lyric.replace(",", "<br>");

			jQuery(this).html(newlyric);
		});
	}



	return {
		'init' : init
	};
})();


jQuery(document).ready(function(){
	MADLIB.init();
});