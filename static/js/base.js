Base = {
    scrollOffset: 650,
    scrollAPI: null,

    watchScroll: function (elem, loadNextPage) {
        Base.scrollAPI = $(elem).data('jsp');
        $(elem).scroll(function () {
            var pos = Base.scrollAPI.getContentPositionY() + Base.scrollOffset;
            var height = Base.scrollAPI.getContentHeight();
            if (pos >= height) {
                loadNextPage();
            }
        });
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
