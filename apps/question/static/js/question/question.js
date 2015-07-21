$(document).ready(function() {

    $('#question-list-table').DataTable();

    $('#question-list-table tbody').on('click', 'tr', function () {

        pk = $(this).attr('id');

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
        document.getElementById("content").scrollIntoView();
        $('#info').css({'opacity':0, 'background-color':'yellow'});
        $('#info').animate({'opacity':1, 'background-color':'white'}, 500);
    });

});