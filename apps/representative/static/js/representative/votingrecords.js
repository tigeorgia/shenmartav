$('#filter-by-vote').change(function (){
    var filter = $(this).find(":selected").attr('name')
    $('#container-votingrecords tr').each(function (){
        if ($(this).attr('class') != filter){
            $(this).hide();
        } else {
            $(this).show();
        }
    })
});