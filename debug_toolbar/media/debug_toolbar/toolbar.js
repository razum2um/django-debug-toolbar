jQuery.noConflict();
jQuery(function($j) {
	var COOKIE_NAME = 'dj_debug_panel';
	$j.djDebug = function(data, klass) {
		$j.djDebug.init();
	}
	$j.extend($j.djDebug, {
		init: function() {
			var current = null;
			$j('#djDebugPanelList li a').click(function() {
				if (!this.className) {
					return false;
				}
				current = $j('#djDebug #' + this.className);
				if (current.is(':visible')) {
				    $j(document).trigger('close.djDebug');
					$j(this).parent().removeClass("active");
				} else {
					//$j('.panelContent').hide();
					$j(document).trigger('close.djDebug');
					current.show();
					$j.djDebug.open();
					$j('#djDebugToolbar li').removeClass("active");
					$j(this).parent().addClass("active");
				}
				return false;
			});
			$j('#djDebug a.close').click(function() {
				$j(document).trigger('close.djDebug');
				return false;
			});
			$j('#djDebug a.remoteCall').click(function() {
				$j('#djDebugWindow').load(this.href, {}, function() {
					$j('#djDebugWindow a.back').click(function() {
						$j(this).parent().parent().hide();
						return false;
					});
				});
				$j('#djDebugWindow').show();
				return false;
			});
			$j('#djDebugTemplatePanel a.djTemplateShowContext').click(function() {
				$j.djDebug.toggle_arrow($j(this).children('.toggleArrow'))
				$j.djDebug.toggle_content($j(this).parent().next());
				return false;
			});
			$j('#djDebugSQLPanel a.djSQLShowStacktrace').click(function() {
				$j.djDebug.toggle_content($j(this).parent().next());
				return false;
			});
			$j('#djHideToolBarButton').click(function() {
				$j.djDebug.hide_toolbar(true);
				return false;
			});
			$j('#djShowToolBarButton').click(function() {
				$j.djDebug.show_toolbar();
				return false;
			});
			if ($j.cookie(COOKIE_NAME)) {
				$j.djDebug.hide_toolbar(false);
			} else {
				$j('#djDebugToolbar').show();
			}
		},
		open: function() {
			$j(document).bind('keydown.djDebug', function(e) {
				if (e.keyCode == 27) {
					$j.djDebug.close();
				}
			});
		},
		toggle_content: function(elem) {
			if (elem.is(':visible')) {
				elem.hide();
			} else {
				elem.show();
			}
		},
		close: function() {
			$j(document).trigger('close.djDebug');
			return false;
		},
		hide_toolbar: function(setCookie) {
		    $j(document).trigger('close.djDebug');
			$j('#djDebugToolbar').hide("fast");
			$j('#djDebugToolbar li').removeClass("active");
			$j('#djDebugToolbarHandle').show();
			if (setCookie) {
				$j.cookie(COOKIE_NAME, 'hide', {
					path: '/',
					expires: 10
				});
			}
		},
		show_toolbar: function() {
			$j('#djDebugToolbarHandle').hide();
			$j('#djDebugToolbar').show("fast");
			$j.cookie(COOKIE_NAME, null, {
				path: '/',
				expires: -1
			});
		},
		toggle_arrow: function(elem) {
            var uarr = String.fromCharCode(0x25b6);
            var darr = String.fromCharCode(0x25bc);
            elem.html(elem.html() == uarr ? darr : uarr);
        }
	});
	$j(document).bind('close.djDebug', function() {
		$j(document).unbind('keydown.djDebug');
		$j('.panelContent').hide()
		$j('#djDebugToolbar li').removeClass("active");
	});
});
jQuery(function() {
	jQuery.djDebug();
});