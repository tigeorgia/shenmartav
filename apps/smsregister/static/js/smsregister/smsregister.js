$(function () {
    $('#id_subscribe_0').on('click', function () {
        $("#form-smsregister").find(':checkbox').prop('checked', this.checked);
    });
});