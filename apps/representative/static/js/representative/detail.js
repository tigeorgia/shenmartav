/*
 * Javascript file for app representative detail
 */

RepresentativeDetail = {
    isLoadingVotingRecord: false,
    hasLoadedVotingRecord: false,


    loadVotingRecordsDone: function () {
        $('#representative #data-text #votingrecords').show();
        Base.enable('#representative');
        RepresentativeDetail.isLoadingVotingRecord = false;
    },


    loadVotingRecords: function () {
        if (RepresentativeDetail.isLoadingVotingRecord) return;
        RepresentativeDetail.isLoadingVotingRecord = true;

        Base.disable('#representative');
        var url = $('#representative #data-text #button-votingrecords').attr('href');
        $.ajax(url, {
            success: function(data, textStatus, jqXHR) {
                $('#representative #data-text #votingrecords').html(data);
                RepresentativeDetail.hasLoadedVotingRecord = true;
            },
            error: function (jqXHR, textStatus, errorThrown) {
                var msg = '<h3>' + jqXHR.status + ' ' + errorThrown + '</h3>';
                $('#representative #data-text #votingrecords').html(msg);
                RepresentativeDetail.loadVotingRecordsDone();
            }
        }).done(RepresentativeDetail.loadVotingRecordsDone);
    },


    setupVotingRecords: function () {
        $('#representative #data-text #button-votingrecords').click(function() {
            var elem = $('#representative #data-text #votingrecords');
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
