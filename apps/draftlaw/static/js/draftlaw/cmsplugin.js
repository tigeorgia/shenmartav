/*
 * Javascript file for cmsplugin draftlaw
 */

DraftLawCMSPlugin = {
    urlQuery: null,
    form: null,
    query: null,
    news: null,
    alert: null,


    setupForm: function () {
        DraftLawCMSPlugin.form.submit(function() {
            // remove form fields interfering with GET
            $('#draftlaw #find #submit').remove();

            // encode text appropriately
            var encoded = encodeURIComponent(DraftLawCMSPlugin.query.val());
            DraftLawCMSPlugin.query.val(encoded.replace(/\ /g, '+'));

            return true;
        });
    },


    setupFind: function () {
        DraftLawCMSPlugin.query.focus(function () {
            $(this).val('');
        });

        DraftLawCMSPlugin.query.autocomplete({
            minLength: 2,
            source: function (req, add) {
                var url = DraftLawCMSPlugin.urlQuery + req.term;
                $.getJSON(url, '', function(data) {
                    var suggestions = [];
                    $.each(data, function(i, val) {
                        suggestions.push(val);
                    });
                add(suggestions);
                });
            },
            select: function (event, ui) {
                DraftLawCMSPlugin.query.val(ui.item.label);
                DraftLawCMSPlugin.form.submit();
                return true;
            }
        });
    },


    loadNewsDone: function (responseText, textStatus, XMLHttpRequest) {
        $('#draftlaw #news #prev').click(function () {
            var url = $(this).attr('href');
            DraftLawCMSPlugin.news.load(url, DraftLawCMSPlugin.loadNewsDone);
            return false;
        });
        $('#draftlaw #news #next').click(function () {
            var url = $(this).attr('href');
            DraftLawCMSPlugin.news.load(url, DraftLawCMSPlugin.loadNewsDone);
            return false;
        });
    },


    setupNews: function () {
        DraftLawCMSPlugin.news = $('#draftlaw #news #item');
        url = URL_DraftLawNews;
        DraftLawCMSPlugin.news.load(url, DraftLawCMSPlugin.loadNewsDone);
    },


    loadAlertDone: function (responseText, textStatus, XMLHttpRequest) {
        $('#draftlaw #alert #prev').click(function () {
            var url = $(this).attr('href');
            DraftLawCMSPlugin.alert.load(url, DraftLawCMSPlugin.loadAlertDone);
            return false;
        });
        $('#draftlaw #alert #next').click(function () {
            var url = $(this).attr('href');
            DraftLawCMSPlugin.alert.load(url, DraftLawCMSPlugin.loadAlertDone);
            return false;
        });
    },


    setupAlert: function () {
        DraftLawCMSPlugin.alert = $('#draftlaw #alert #item');
        url = URL_DraftLawAlert;
        DraftLawCMSPlugin.alert.load(url, DraftLawCMSPlugin.loadAlertDone);
    },


    setup: function () {
        DraftLawCMSPlugin.urlQuery = URL_DraftLawQuery.slice(0,
            URL_DraftLawQuery.length - 2) // slice off '0/'
        DraftLawCMSPlugin.form = $('#draftlaw #find form');
        DraftLawCMSPlugin.query = $('#draftlaw #find #query');

        DraftLawCMSPlugin.setupForm();
        DraftLawCMSPlugin.setupFind();
        DraftLawCMSPlugin.setupNews();
        DraftLawCMSPlugin.setupAlert();
    }
};



$(function () {
    DraftLawCMSPlugin.setup();
});
