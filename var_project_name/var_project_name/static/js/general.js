/*jshint unused: false*/
function get_screen_size() {
    // Returns the current screen size in Bootstrap 3 terms
    // See http://stackoverflow.com/a/19462847
    //
    var envValues = ['xs', 'sm', 'md', 'lg'];
    var $el = $('<div></div>');
    $el.appendTo($('body'));
    for (var i = envValues.length - 1; i >= 0; i--) {
        $el.addClass('hidden-'+envValues[i]);
        if ($el.is(':hidden')) {
            $el.remove();
            return envValues[i];
        }
    }
}
/*jshint unused: true*/

function init_carousel(elements) {
    // Carousel
    elements.carousel({
        interval: 7000
    });
}

function init_popover(elements) {
    // Popover
    elements.popover({
        placement: 'top'
        ,trigger: 'hover'
        ,html: true
    }).css('cursor', 'pointer');
}

function init_textarea(elements) {
    // Textarea auto-expand
    elements.css('overflow', 'hidden').autogrow();
}

function init_tabs() {
    // show active tab on reload
    if (location.hash !== '') $('a[href="' + location.hash + '"]').tab('show');

    // remember the hash in the URL without jumping
    $('a[data-toggle="tab"]').on('shown.bs.tab', function(e) {
        if(history.pushState) {
            history.pushState(null, null, '#'+$(e.target).attr('href').substr(1));
        } else {
            location.hash = '#'+$(e.target).attr('href').substr(1);
        }
    });
}

function init_tooltip(elements) {
    // Tooltip
    elements.tooltip({
        placement: 'bottom'
    });
}

function init_spinner(elements) {
    // Spinner
	elements.spin({
		lines: 11
		,length: 5
		,width: 4
		,radius: 10
		,corners: 1.0
		,rotate:0
		,trail: 62
		,speed: 1.0
		,direction: 1
	});
}

function init_form(form) {
    if (!form.find('[data-class="spinner"]').length) form.prepend('<div class="spinner" data-class="spinner"></div>');
	form.change(function() {
		if (form.find('input[type=file]').length) {
			var input, file;

			// (Can't use `typeof FileReader === "function"` because apparently
			// it comes back as "object" on some browsers. So just see if it's there
			// at all.)
			if (!window.FileReader) {
				$('<div class="alert alert-danger">' + gettext("The file API isn't supported on this browser yet.") + '</alert>').insertAfter(input);
				return;
			}

			input = form.find('input[type=file]');
			if (!input[0].files) {
				$('<div class="alert alert-danger">' + gettext("This browser doesn't seem to support the 'files' property of file inputs.") + '</div>').insertAfter(input);
			}
			else if (!input[0].files[0]) {
				input.parents('.form-group').find('.alert').remove();
			}
			else {
				file = input[0].files[0];
				// 5MB -> 5120KB -> 5242880
				if (file.size > 5242880) {
					$('<div class="alert alert-danger">' + gettext('The file is too large. Please select a smaller image (< 5mb).') + '</div>').insertAfter(input);
					input[0].parentNode.replaceChild(
						input[0].cloneNode(true),
						input[0]
					);
				} else {
					input.parents('.form-group').find('.alert').remove();
				}
			}
		}
	});
    form.submit(function() {
        form.find('[data-class="spinner"]').show();
    });
	init_spinner($('[data-class="spinner"]'));
}

// Document loaded and ready.
$(document).ready(function() {
    init_popover($('[data-class="popover"]'));
    init_tabs();
    init_tooltip($('[data-class="tooltip"]'));
    init_textarea($('textarea'));
	init_spinner($('[data-class="spinner"]'));
	$('form').each(function() {
		init_form($(this));
	});
    // Use this in in the template that has a carousel slider
    // init_carousel($('[data-class="carousel"]'));
    
    // Detect unsaved changes
    if ($('form[data-class="detect-changes"]').length) {
    	var unsaved = false;
	$('form[data-class="detect-changes"]').each(function () {
	    var form = $(this);
	    form.on('change keyup', 'input, textarea, select', function () {
	        unsaved = true;
	    });
	    form.submit(function() {
	        unsaved = false;
	    });
	});

        $(window).bind('beforeunload', function () {
            if (unsaved) {
                return gettext("You have unsaved changes on this page. Do you want to leave this page and discard your changes?");
            }
        });
    }
});

// If objects are added to the DOM after document ready.
$(document).on('DOMNodeInserted', function(e) {
    init_popover($(e.target).find('[data-class="popover"]'));
    init_tooltip($(e.target).find('[data-class="tooltip"]'));
    init_textarea($(e.target).find('textarea'));
	init_spinner($(e.target).find('[data-class="spinner"]'));
	$(e.target).find('form').each(function() {
		init_form($(this));
	});
    init_carousel($(e.target).find('[data-class="carousel"]'));
});
