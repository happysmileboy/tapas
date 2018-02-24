/**
 * EFFECTS:
 *
 * "responsive:slide"
 ** Displays one frame at the time.
 ** The height adjusts to currently displayed frame automatically (may reflow the contents bellow upon change).
 ** The width of one element inside Theatre is supposed to be 100%.
 ** If you need spaces between frames use margin-right on .theatre-actor .
 * "responsive:filmstrip"
 ** Can display multiple .theatre-actor blocks at the time (depends on your widths)
 ** The height will be same as the tallest block (no contents reflow upon change)
 ** The width of one element is fully customizable - multiple elements may fit in the view (eg. .col-lg-4)
 *
 * @package    Elixon Theatre
 * @subpackage Responsive
 * @author     Daniel Sevcik <sevcik@webdevelopers.cz>
 * @version    $Revision: 1.0 $
 * @copyright  2014 Daniel Sevcik
 * @since      2014-04-30 15:48:23 UTC
 * @access     public
 */
(function($) {
	function responsiveSlide($stage, $actors, settings, theatre) {
		//var slideOffset=120; // 100: there are not margins around page so it looks ugly

		this.capable=function() { // return true or failover effect name
			return true;
		};
		this.init=function() {
			$stage.addClass("theatre-responsive theatre-responsive-fx1");
			$actors.eq(theatre.index).addClass("active");
		};
		// this.next=function(prevPos) {
		//	console.log('next()', arguments, theatre);
		// };
		// this.prev=function(prevPos) {
		//	console.log('prev()', arguments, theatre);
		// };
		this.jump=function(prevPos) {
			if (prevPos == theatre.index) return; // just redraw/resize event: not relevant for responsive designs

			// console.log('Responsive jump()', prevPos, ' => ', theatre.index);
			var $this=$(this);
			var $prev=$actors.eq(prevPos);
			var $next=$actors.eq(theatre.index);

			var slideOffset=Math.ceil($prev.outerWidth() / $prev.innerWidth() * 100);

			// Animation effect
			var prevHeight=$prev.outerHeight();
			var nextHeight=$next.outerHeight();
			var dir=(prevPos < theatre.index ? 1 : -1);
			if (theatre.settings.playDir == "prev") dir*=-1;

			$stage
				.addClass("in-transition")
				.height(prevHeight);

			$next
				.addClass("fade-in");
			$prev
				.addClass("fade-out");

			switch (theatre.settings.animation) {
			case "slide":
				$next
					.css("left", (dir * slideOffset) + "%");
			$prev.stop(true, true).animate({"left": (-1 * dir * slideOffset) + "%"}, theatre.settings.speed, function() {
				$(this).removeClass("fade-out").css("left", "");
			});
			$next.stop(true, true).animate({"left": "0%"}, theatre.settings.speed, function() {
				$(this).removeClass("fade-in").css("left", "");
			});
				break;
			case "fade":
				$next.fadeIn(0);
				$prev.stop(true, true).fadeOut(theatre.settings.speed, function() {
					$next.removeClass("fade-in");
					$prev.removeClass("fade-out");
				});
				break;
			};

			$stage.stop(true, true).animate({"height": nextHeight + "px"}, theatre.settings.speed, function() {
				$(this).removeClass("in-transition").height("auto");
				theatre.methods.onAfterMove.apply($(this));
			});

			// Final
			$actors
				.not($next.addClass("active"))
				.removeClass("active");
		};
		this.destroy=function() {
			$stage.removeClass("theatre-responsive theatre-responsive-fx1 in-transition");
			$actors.removeClass("active fade-in fade-out");
		};
	}

	$.fn.theatre('effect', 'responsive:slide', function ($stage, $actors, settings, theatre) {
		settings['animation']='slide';
		responsiveSlide.call(this, $stage, $actors, settings, theatre);
	});
	$.fn.theatre('effect', 'responsive:fade', function ($stage, $actors, settings, theatre) {
		settings['animation']='fade';
		responsiveSlide.call(this, $stage, $actors, settings, theatre);
	});
	//------------------------------------------------------------------------

	$.fn.theatre('effect', 'responsive:filmstrip', function($stage, $actors, settings, theatre) {
		var offset=0; // 100: there are not margins around page so it looks ugly
		var $container;

		this.capable=function() { // return true or failover effect name
			return $.fn.theatre.cssSupport('display', 'inline-block') ? true : 'horizontal';
		};
		this.init=function() {

			$stage.addClass("theatre-responsive");
			$actors.eq(theatre.index).addClass("active");

			$container=$("<div class='theatre-container'></div>");

			$actors.parent().append($container);
			$container.append($actors);
		};

		this.prev=function(prevPos) {
			if (prevPos == theatre.index) return; // just redraw/resize event: not relevant for responsive designs
			var $prev=$actors.eq(prevPos);
			var $next=$actors.eq(theatre.index);
			var left=$next.outerWidth();

			$stage.addClass("in-transition");
			$container.prepend($next).css({left: -left+"px"});
			$container.stop(true, true).animate({left: '0px'}, theatre.settings.speed, function() {
				$stage.removeClass("in-transition");
				theatre.methods.onAfterMove.apply($stage);
			});

			// Final
			$actors
				.not($next.addClass("active"))
				.removeClass("active");
		};

		this.next=function(prevPos) {
			if (prevPos == theatre.index) return; // just redraw/resize event: not relevant for responsive designs
			var $prev=$actors.eq(prevPos);
			var $next=$actors.eq(theatre.index);
			var left=$prev.outerWidth();

			$stage.addClass("in-transition");
			$container.stop(true, true).animate({left: -left+'px'}, theatre.settings.speed, function() {
				$container.append($prev).css({left: "0px"});
				$stage.removeClass("in-transition");
				theatre.methods.onAfterMove.apply($stage);
			});

			// Final
			$actors
				.not($next.addClass("active"))
				.removeClass("active");
		};
		// this.jump=function(prevPos) {
		//	var $prev=$actors.eq(prevPos);
		//	var $next=$actors.eq(theatre.index);
		//
		//	var left=0;
		//	$next.prevAll(".theatre-actor").each(function(k, v) {
		//		left+=$(v).outerWidth();
		//	});
		//
		//	$stage
		//		.addClass("in-transition");
		//
		//	$container.stop(true, true).animate({left: -left+'px'}, theatre.settings.speed, function() {$stage.removeClass("in-transition");});
		//
		//	// Final
		//	$actors
		//		.not($next.addClass("active"))
		//		.removeClass("active");
		// };
		this.destroy=function() {
			$stage.removeClass("theatre-responsive in-transition");
			$actors.removeClass("active");

			if ($container) {
				$container.parent().append($actors);
				$container.remove();
			}
		};
	});
})(jQuery);
