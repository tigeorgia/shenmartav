/*
 * Javascript file for question list
 */

QuestionList = {
    isLoadingInfo: false,
    isLoadingNextPage: false,
    urlInfo: null,
    urlItems: null,
    nextPage: 1,
    scrollOffset: 50,


    setInfoDone: function () {
        Base.enable('#question');
        QuestionList.isLoadingInfo = false;
    },


    setInfo: function (elem) {
        if (QuestionList.isLoadingInfo) return;
        QuestionList.isLoadingInfo = true;

        pk = $(elem).attr('id');
        pk = parseInt(pk.slice(5, pk.length)); // 5 == 'item-'
        if (!pk) {
            QuestionList.isLoadingInfo = false;
            return;
        }

        Base.disable('#question');
        $('.item').removeClass('item-selected');
        $(elem).addClass('item-selected');

        $.ajax(QuestionList.urlInfo + pk + '/', {
            success: function(data, textStatus, jqXHR) {
                $('#question #info').html(data);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                var msg = '<h3>' + jqXHR.status + ' ' + errorThrown + '</h3>';
                $('#question #info').html(msg);
                QuestionList.setInfoDone();
            }
        }).done(QuestionList.setInfoDone);
    },



    hoverIntentQuestions: function () {
        $('#question #list .item').hoverIntent(
            function () { QuestionList.setInfo($(this)); },
            function () {}
        );
    },


    selectFromLocation: function () {
        var hash = window.location.hash;
        // 6 == #item-
        var pk = parseInt(hash.slice(6, hash.length));
        if (!pk) return;

        var elem = $('#question #list #item-' + pk);
        QuestionList.setInfo($(elem));
    },


    loadNextPageDone: function () {
        $('#question #list table').trigger('update');
        QuestionList.selectFromLocation();
        Base.enable('#question');
        QuestionList.isLoadingNextPage = false;
    },


    loadNextPage: function () {
        if (QuestionList.isLoadingNextPage) return;
        QuestionList.isLoadingNextPage = true;

        Base.disable('#question');

        var url = QuestionList.urlItems + QuestionList.nextPage + '/';
        $.ajax(url, {
            success: function(data, textStatus, jqXHR) {
                if (data) {
                    if (QuestionList.nextPage == 1) {
                        $('#question #list #items').html(data);
                    } else {
                        $('#question #list #items').append(data);
                    }

                    QuestionList.nextPage += 1;
                    QuestionList.hoverIntentQuestions();
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                var msg = '<tr><td><h3>' + jqXHR.status + ' ' + errorThrown + '</h3></td></tr>';
                $('#question #list #items').html(msg);
                QuestionList.loadNextPageDone();
            }
        }).done(QuestionList.loadNextPageDone);
    },


    watchScroll: function () {
        $('#question #list').scroll(function () {
            var pos = $(this).scrollTop() + $(this).height() + QuestionList.scrollOffset;
            var height = $('#question #list #items').height();
            if (pos >= height) {
                QuestionList.loadNextPage();
            }
        });
    },


    setup: function () {
        // slice off '0/'
        QuestionList.urlInfo = URL_QuestionInfo.slice(0,
            URL_QuestionInfo.length - 2);
        QuestionList.urlItems = URL_QuestionItems.slice(0,
            URL_QuestionItems.length - 2);

        QuestionList.hoverIntentQuestions();
        QuestionList.watchScroll();

        $('#question #list table').tablesorter();
        QuestionList.loadNextPage();
    }
};


$(function () {
    QuestionList.setup();
});
