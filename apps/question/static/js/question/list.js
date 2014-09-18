/*
 * Javascript file for question list
 */

QuestionList = {
    isLoadingInfo: false,
    isLoadingNextPage: false,
    urlInfo: null,
    urlItems: null,
    nextPage: 1,


    selectRepresentativeAskForm: function () {
        var name = $('#question #info #questionee #representative-name').html();
        var select = $('#question #ask #id_representative');
        $('#question #ask #id_representative > option').each(function () {
            if ($(this).text() == name) {
                select.val($(this).val());
                return false;
            }
        });
    },


    setInfoDone: function () {
        QuestionList.selectRepresentativeAskForm();
        Base.enable('#question #info');
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

        Base.disable('#question #info');
        $('.item').removeClass('item-selected');
        $(elem).addClass('item-selected');

        $.ajax(QuestionList.urlInfo + pk + '/', {
            success: function (data, textStatus, jqXHR) {
                $('#question #info').html(data);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                var msg = '<h3>' + jqXHR.status + ' ' + errorThrown + '</h3>';
                $('#question #info').html(msg);
                QuestionList.setInfoDone();
            }
        }).done(QuestionList.setInfoDone);
    },


    selectQuestion: function () {
        $('#question #list .item').click(
            function () {
                QuestionList.setInfo($(this));
            }
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
        Base.setHeightScrollPane('#question', '#question #list', 100);
        Base.scrollAPI.reinitialise();
        Base.enable('#question #list');
        QuestionList.isLoadingNextPage = false;
    },


    loadNextPage: function () {
        if (QuestionList.isLoadingNextPage) return;
        QuestionList.isLoadingNextPage = true;

        Base.disable('#question #list');

        var url = QuestionList.urlItems + QuestionList.nextPage + '/';
        $.ajax(url, {
            success: function (data, textStatus, jqXHR) {
                if (data) {
                    if (QuestionList.nextPage == 1) {
                        $('#question #list #items').html(data);
                    } else {
                        $('#question #list #items').append(data);
                    }

                    QuestionList.nextPage += 1;
                    QuestionList.selectQuestion();
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                var msg = '<tr><td><h3>' + jqXHR.status + ' ' + errorThrown + '</h3></td></tr>';
                $('#question #list #items').html(msg);
                QuestionList.loadNextPageDone();
            }
        }).done(QuestionList.loadNextPageDone);
    },


    setup: function () {
        // slice off '0/'
        QuestionList.urlInfo = URL_QuestionInfo.slice(0,
            URL_QuestionInfo.length - 2);
        QuestionList.urlItems = URL_QuestionItems.slice(0,
            URL_QuestionItems.length - 2);

        QuestionList.selectQuestion();
        Base.watchScroll('#question #list', QuestionList.loadNextPage);
        $('#question #list table').tablesorter();
        QuestionList.loadNextPage();
    }
};


$(function () {
    QuestionList.setup();
});
