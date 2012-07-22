Base = {
    scrollPercentage: .95,
    scrollAPI: null,

    /* timeout business coz scrolling often fires +
       may result in flicker if pages are loaded quickly, too */
    scrollTimedOut: true,
    scrollTimeOutDelay: 300,
    scrollTimeOut: function () {
        Base.scrollTimedOut = true;
    },


    watchScroll: function (elem, loadNextPage) {
        Base.scrollAPI = $(elem).data('jsp');
        $(elem).scroll(function () {
            var scrolled = Base.scrollAPI.getPercentScrolledY();
            if (scrolled >= Base.scrollPercentage && Base.scrollTimedOut) {
                loadNextPage();
                Base.scrollTimedOut = false;
                window.setTimeout('Base.scrollTimeOut()', Base.scrollTimeOutDelay);
            }
        });
    },


    setHeightScrollPane: function (ref, elem, height) {
        var total = parseInt($(ref).css('height'));
        var target = (total * height / 100.) + 'px';
        $(elem).css('height', target);
        $(elem).data('jsp').reinitialise();
    },


    enable: function (elem) {
        elem = $(elem);
        elem.fadeTo('fast', 1);
        $('#header #logo #wheel').removeClass('rotate');
        elem.removeClass('wait');
    },


    disable: function (elem) {
        elem = $(elem);
        elem.addClass('wait');
        $('#header #logo #wheel').addClass('rotate');
        elem.fadeTo('fast', .3);
    },


    setup: function () {
        $('.scroll-pane').jScrollPane({
            verticalDragMinHeight: 40,
            verticalDragMaxHeight: 40,
        });
    },
}

$(function() {
    Base.setup()
})
