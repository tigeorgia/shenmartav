/*
 * Javascript file for draftlaw list
 */

DraftLawList = {
    items: null,
    info: null,
    isLoadingInfo: false,
    isLoadingNextPage: false,
    nextPage: 1,
    previousQuery: null,


    setInfoDone: function () {
        Base.setHeightScrollPane('#draftlaw', '#draftlaw #container-info', 100);
        Base.enable('#draftlaw #info');
        DraftLawList.isLoadingInfo = false;
    },


    setInfo: function (elem) {
        if (DraftLawList.isLoadingInfo) return;
        DraftLawList.isLoadingInfo = true;

        pk = $(elem).attr('id');
        pk = parseInt(pk.slice(5, pk.length)); // 5 == 'item-'
        if (!pk) {
            DraftLawList.isLoadingInfo = false;
            return;
        }

        Base.disable('#draftlaw #info');
        $('.item').removeClass('item-selected');
        $(elem).addClass('item-selected');

        $.ajax(DraftLawList.urlInfo + pk + '/', {
            success: function(data, textStatus, jqXHR) {
                DraftLawList.info.html(data);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                var msg = '<h3>' + jqXHR.status + ' ' + errorThrown + '</h3>';
                DraftLawList.info.html(msg);
                DraftLawList.setInfoDone();
            }
        }).done(DraftLawList.setInfoDone);
    },


    hoverIntentDraftLaws: function () {
        $('#draftlaw #items .item').hoverIntent(
            function () { DraftLawList.setInfo($(this)); },
            function () {}
        );
    },


    getNextPageURL: function () {
        var url = ''
        var query = $('#draftlaw #search #data').val();

        if (!query) { // look in GET param
            var idx_params = window.location.href.indexOf('?') + 1;
            var hashes = window.location.href.slice(idx_params).split('&');
            for (var i = 0; i < hashes.length; i++) {
                hash = hashes[i].split('=');
                if (hash[0] == 'query') {
                    query = decodeURIComponent(hash[1]).replace(/\+/g, ' ');
                    query = query.replace(/%20/g, ' ');
                    $('#draftlaw #search #data').val(query);
                    break;
                }
            }
        }

        if (query) {
            if (query != DraftLawList.previousQuery) {
                DraftLawList.nextPage = 1;
                DraftLawList.previousQuery = query;
            }
            url = DraftLawList.urlItems + DraftLawList.nextPage + '/' + query + '/';
        } else {
            url = DraftLawList.urlItems + DraftLawList.nextPage + '/';
        }

        return url;
    },


    loadNextPageDone: function () {
        $('#draftlaw #list .item').click(function() {
            DraftLawList.setInfo($(this));
        });

        $('#draftlaw #list table').trigger('update');
        Base.setHeightScrollPane('#draftlaw', '#draftlaw #container-list', 90);
        Base.enable('#draftlaw #list');
        DraftLawList.isLoadingNextPage = false;
    },


    loadNextPage: function () {
        if (DraftLawList.isLoadingNextPage) return;
        DraftLawList.isLoadingNextPage = true;

        Base.disable('#draftlaw #list');

        var url = DraftLawList.getNextPageURL();
        $.ajax(url, {
            success: function(data, textStatus, jqXHR) {
                if (data) {
                    if (DraftLawList.nextPage == 1) {
                        DraftLawList.items.html(data);
                    } else {
                        DraftLawList.items.append(data);
                    }

                    DraftLawList.nextPage += 1;
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                var msg = '<li><h3>' + jqXHR.status + ' ' + errorThrown + '</h3></li>';
                DraftLawList.items.html(msg);
                DraftLawList.loadNextPageDone();
            }
        }).done(DraftLawList.loadNextPageDone);
    },


    setupSearch: function () {
        $('#draftlaw #search').submit(function () {
            DraftLawList.loadNextPage();
            return false;
        });

        $('#draftlaw #search #reset').click(function () {
            //$('#draftlaw #search-data').val(''); doesn't set value?
            $('#draftlaw #search #data').val(' ');
            DraftLawList.nextPage = 1;
            DraftLawList.loadNextPage();
            return false;
        });
    },


    setup: function() {
        DraftLawList.urlInfo = URL_DraftLawInfo.slice(0,
            URL_DraftLawInfo.length - 2); // slice off '0/'
        DraftLawList.urlItems = URL_DraftLawItems.slice(0,
            URL_DraftLawItems.length - 2); // slice off '0/'
        DraftLawList.items = $('#draftlaw #items');
        DraftLawList.info = $('#draftlaw #info');

        DraftLawList.setupSearch();

        Base.watchScroll('#draftlaw #container-list', DraftLawList.loadNextPage);
        $('#draftlaw #list table').tablesorter();

        DraftLawList.loadNextPage();
    }
};



$(function () {
    DraftLawList.setup();
});
