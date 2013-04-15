$(document).ready(function() {
	
	
	

	$("#mps-row1").carouFredSel({
		auto: false,
		synchronise	: [
			["#mps-row2", true, true, 0],
			["#mps-row3", true, true, 0],
			],
		prev: {
			button: '#scroll-prev',
			key: 'left',
			items: 3,
			easing : "easeInBack",
			duration: 800,
		},
		next: {
			button: '#scroll-next',
			key: 'right',
			items: 3,
			easing : "easeInBack",
			duration: 800,
		},
		scroll: 5,
	});
	
	
	$("#mps-row2").carouFredSel({
		auto		: false
	});
	
	$("#mps-row3").carouFredSel({
		auto		: false
	});
	
});
