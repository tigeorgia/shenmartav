$(document).ready(
		function() {

			// Create mp slider
			$("#mps-row1").carouFredSel(
					{
						auto : false,
						// This will synchronize all 3 rows to load and scroll
						synchronise : [ [ "#mps-row2", true, true, 0 ],
								[ "#mps-row3", true, true, 0 ], ],
						prev : {
							button : '#scroll-prev',
							key : 'left',
							items : 3,
							easing : "easeInBack",
							duration : 800,
						},
						next : {
							button : '#scroll-next',
							key : 'right',
							items : 3,
							easing : "easeInBack",
							duration : 800,
						},
						// Load all visible images
						onCreate : function(data) {
							data.items.each(function() {
								loadMpImg($(this));
							});
						},
						scroll : {
							items : 5,
							// Load images when scrolling is active
							onAfter : function(data) {
								data.items.visible.each(function() {
									loadMpImg($(this));
								});
							}
						},

					});
			// Now define 2nd and 3rd rows
			$("#mps-row2").carouFredSel({
				auto : false,
				onCreate : function(data) {
					data.items.each(function() {
						loadMpImg($(this));
					});
				},

			});

			$("#mps-row3").carouFredSel({
				auto : false,
				onCreate : function(data) {
					data.items.each(function() {
						loadMpImg($(this));
					});
				},
			});

			// Get data-src and set it as src to slider items
			function loadMpImg($image) {
				$image = $image.find('img');
				$imgsrc = $image.data('mpimage');
				$image.attr('src', $imgsrc);
			}
			
			$("#mp-stats-slider").carouFredSel({
				direction: "up",
				items: 1,
				width: 268,
			});

		});
