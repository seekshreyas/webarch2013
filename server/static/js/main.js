var MADLIB = MADLIB || {};

MADLIB = (function(){


	var init = function(){
		console.log("page loaded");

		// parseLyrics();
		evtHandler();
	};


	//Event Handler
	function evtHandler(){
		jQuery('#madlib-input').submit(function(event){
			event.preventDefault();
			
			// validateForm(jQuery(this));
		});
	}


	function validateForm(elem){
		// caching element selection for DOM seek efficiency
		// console.log(elem);
		// jQuery('#madlib-input').submit();
	
	}



	function getFormVal(){
		

		return {
			'teachname' : jQuery('#field-txt').val(),
			'favnum' :jQuery('#field-num').val(),
			'petname' :jQuery('input[type=radio]:checked').val(),
			'jamname' :jQuery('#field-dropdown').val()
		};

	}


	return {
		'init' : init
	};
})();


jQuery(document).ready(function(){
	MADLIB.init();
});