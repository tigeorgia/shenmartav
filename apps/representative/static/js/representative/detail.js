/*
 * Javascript file for app representative detail
 */

RepresentativeDetail = {
    isLoadingVotingRecord: false,
    hasLoadedVotingRecord: false,


    loadVotingRecordsDone: function () {
        $('#representative #container-votingrecords').show();
        $('#representative #container-votingrecords').data('jsp').reinitialise();
        $('#representative').data('jsp').reinitialise();
        Base.enable('#representative');
        RepresentativeDetail.isLoadingVotingRecord = false;
    },


    loadVotingRecords: function () {
        if (RepresentativeDetail.isLoadingVotingRecord) return;
        RepresentativeDetail.isLoadingVotingRecord = true;

        Base.disable('#representative');
        $.ajax(URL_Votingrecords, {
            success: function(data, textStatus, jqXHR) {
                $('#representative #votingrecords').html(data);
                RepresentativeDetail.hasLoadedVotingRecord = true;
            },
            error: function (jqXHR, textStatus, errorThrown) {
                var msg = '<h3>' + jqXHR.status + ' ' + errorThrown + '</h3>';
                $('#representative #votingrecords').html(msg);
                RepresentativeDetail.loadVotingRecordsDone();
            }
        }).done(RepresentativeDetail.loadVotingRecordsDone);
    },


    setupVotingRecords: function () {
        $('#representative #data-text #button-votingrecords').click(function() {
            var elem = $('#representative #container-votingrecords');
            if ($(elem).is(":visible")) {
                $(elem).hide();
            } else {
                if (!RepresentativeDetail.hasLoadedVotingRecord) {
                    RepresentativeDetail.loadVotingRecords();
                } else {
                    $(elem).show();
                }
            }
            return false;
        });
    },


    setupAttendanceIncome: function () {
        $('#representative #data-boxes #attendance h2').addClass('heading');
        $('#representative #data-boxes #income h2').addClass('heading');
    },


    setup: function () {
        RepresentativeDetail.setupVotingRecords();
        RepresentativeDetail.setupAttendanceIncome();
    }
};



$(function () {
    RepresentativeDetail.setup();
});
