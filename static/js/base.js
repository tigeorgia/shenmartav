Base = {
    enable: function (elem) {
        elem = $(elem);
        elem.fadeTo('fast', 1);
        $('#header #logo').removeClass('rotate');
        elem.removeClass('wait');
    },


    disable: function (elem) {
        elem = $(elem);
        elem.addClass('wait');
        $('#header #logo').addClass('rotate');
        elem.fadeTo('fast', .3);
    },


    setup: function () {
    },
}

$(function() {
    Base.setup()
})
