function init_carousel(selector) {
    // Carousel
    selector.carousel({
        interval: 7000
    });
}

function init_popover(selector) {
    // Popover
    selector.popover({
        placement: 'bottom'
        ,trigger: 'hover'
    });
}

function init_textarea(selector) {
    // Textarea auto-expand
    selector.css('overflow', 'hidden').autogrow();
}

function init_tooltip(selector) {
    // Tooltip
    selector.tooltip({
        placement: 'bottom'
    });
}

// Document loaded and ready.
$(document).ready(function() {
    init_popover($('[data-class="popover"]'));
    init_tooltip($('[data-class="tooltip"]'));
    init_textarea($('textarea'));
    init_carousel($('[data-class="carousel"]'));
});

// If objects are added to the DOM after document ready.
$(document).on('DOMNodeInserted', function(e) {
    init_popover($(e.target).find('[data-class="popover"]'));
    init_tooltip($(e.target).find('[data-class="tooltip"]'));
    init_textarea($(e.target).find('textarea'));
    init_carousel($(e.target).find('[data-class="carousel"]'));
});