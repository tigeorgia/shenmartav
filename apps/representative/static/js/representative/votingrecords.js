$('#filter-by-vote').change(function (){
    var filter = $(this).find(":selected").attr('name');
    var pane = $('.scroll-pane');
    pane.jScrollPane();
    var api = pane.data('jsp');

    $('#container-votingrecords tr').each(function (){
        if ($(this).attr('class') != filter){
            $(this).hide();
        } else {
            $(this).show();
        }
    });

    api.reinitialise();
});