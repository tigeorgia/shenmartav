/*
 * Javascript file for cmsplugin Question
 */
QuestionCMSPlugin = {
    setActionSubmit: function () {
        var action = $('#question #ask form').attr('action');
        var val = $('#question #ask select').val();
        action = action.replace('0', val)
        $('#question #ask form').attr('action', action);
        $('#question #ask form').submit();
    },


    setup: function () {
        $('#question #ask select').change(function() {
            QuestionCMSPlugin.setActionSubmit();
        });
        $('#question #ask input').click(function() {
            QuestionCMSPlugin.setActionSubmit();
            return false;
        });
    }
};



$(function () {
    QuestionCMSPlugin.setup();
});
