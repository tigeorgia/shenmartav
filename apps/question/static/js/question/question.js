$(document).ready(function() {

    $('#question-list-table').DataTable();

    $('#question #list .item').click(function () {

        pk = $(this).attr('id');
        //pk = parseInt(pk.slice(5, pk.length)); // 5 == 'item-'

        if (!pk) {
            return;
        }

        $('.item').removeClass('item-selected');
        $(this).children().removeClass('sorting_1');
        $(this).addClass('item-selected');

        $.ajax("/questions/info/" + pk + '/', {
            success: function (data, textStatus, jqXHR) {
                $('#question #info').html(data);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                var msg = '<h3>' + jqXHR.status + ' ' + errorThrown + '</h3>';
                $('#question #info').html(msg);
            }
        }).done();
    });

});