/*
 * Javascript file for cmsplugin Representative
 */

RepresentativeCMSPlugin = {
    urlQuery: '',
    from: null,
    query: null,


    setupForm: function () {
        RepresentativeCMSPlugin.form.submit(function() {
            // remove form fields interfering with GET
            RepresentativeCMSPlugin.query.remove();
            $('#representative #find #submit').remove();
            return true;
        });
    },


    setupFind: function () {
        RepresentativeCMSPlugin.query.focus(function () {
            $(this).val('');
        });

        RepresentativeCMSPlugin.query.autocomplete({
            minLength: 2,
            source: function (req, add) {
                var url = RepresentativeCMSPlugin.urlQuery + encodeURIComponent(req.term) + '/';
                $.getJSON(url, '', function(data) {
                    var suggestions = [];
                    $.each(data, function(i, val) {
                        suggestions.push(val);
                    });
                    add(suggestions);
                });
            },
            select: function (event, ui) {
                var form = RepresentativeCMSPlugin.form;
                var action = $(form).attr('action') + '#member-' + ui.item.pk;
                $(form).attr('action', action);

                RepresentativeCMSPlugin.query.val(ui.item.label);
                RepresentativeCMSPlugin.form.submit();

                return true;
            }
        });
    },


    setup: function () {
        RepresentativeCMSPlugin.urlQuery = URL_RepresentativeQuery.slice(0,
            URL_RepresentativeQuery.length - 2) // slice off '0/'
        RepresentativeCMSPlugin.form = $('#representative #find form');
        RepresentativeCMSPlugin.query = $('#representative #find #query');

        RepresentativeCMSPlugin.setupForm();
        RepresentativeCMSPlugin.setupFind();
    }
};



$(function () {
    RepresentativeCMSPlugin.setup();
});
