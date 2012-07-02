/*
 * Javascript file for app Representative
 */

RepresentativeFind = {
    isLoadingMemberInfo: false,
    isLoadingUnit: false,
    empty: '/static/img/empty.png',
    memberInfoTop: 0,
    unit: {
        'parliament': null,
        'ajara': null,
        'tbilisi': null,
    },
    activeUnit: null,
    noneSelected: '',
    urlMemberInfo: null,
    showOfferFulltextSearch: false,
    inputDelay: 2000,
    inputTime: 0,
    reallySubmitSearch: false,
    hoverInterval: 300,


    filterElectionType: function (type) {
            $('#representative #filter-text').val('');
            $('#representative #filter-party').val('all');

            console.log(type);
            if (type == 2) {
                console.log('majori');
                $('#representative .member.majoritarian').show();
                $('#representative .member.partylist').hide();
            } else if (type == 1) {
                $('#representative .member.partylist').show();
                $('#representative .member.majoritarian').hide();
            } else {
                $('#representative .member.majoritarian').show();
                $('#representative .member.partylist').show();
            }
    },


    filterInput: function (form) {
        $('#representative #filter-electiontype').val('0');
        $('#representative #filter-party').val('all');

        var data = $('#representative #filter-text').val().toLowerCase();
        var members = $('#representative .member');
        members.hide();
        members.each(function() {
            if ($(this).hasClass('party-' + data) ||
                $(this).html().indexOf(data) != -1) {
                $(this).show();
                // don't break out: show more results
            }
        });

        if ($('#representative #members .member:visible').length == 0 ||
            RepresentativeFind.showOfferFulltextSearch) {
            $('#representative #select #offer-fulltext-search').show();
        } else {
            $('#representative #select #offer-fulltext-search').hide();
        }
    },


    setupFiltersParty: function () {
        $('#representative #filter-party').change(function() {
            $('#representative #filter-text').val('');
            $('#representative #filter-electiontype').val('0');
            var val = $(this).val();
            if (val == 'all') {
                $('#representative .member').show();
            } else {
                $('#representative .member').hide();
                $('#representative .member.' + val).show();
            }
        });
    },


    checkInput: function () {
        var threshold = new Date().getTime()- RepresentativeFind.inputDelay;
        if (threshold >= RepresentativeFind.inputTime) {
            $('#representative #offer-fulltext-search').show();
        }
    },


    setupFilters: function () {
        $('#representative #select #filter-electiontype').change(function () {
            RepresentativeFind.filterElectionType($(this).val());
        });

        $('#representative #select form').submit(function() {
            if (RepresentativeFind.reallySubmitSearch) {
                return true;
            } else {
                RepresentativeFind.showOfferFulltextSearch = true;
                RepresentativeFind.filterInput($(this));
                return false;
            }
        });

        $('#representative #select #filter-text').keyup(function(event) {
            if (event.which != 13) { // not enter key
                RepresentativeFind.showOfferFulltextSearch = false;
            }
            RepresentativeFind.filterInput($(this).parent());
            RepresentativeFind.inputTime = new Date().getTime();
            setTimeout(RepresentativeFind.checkInput, RepresentativeFind.inputDelay);
        });

        $('#representative #select #offer-fulltext-search').click(function () {
            RepresentativeFind.reallySubmitSearch = true;
            $('#representative #select #filter-submit').click();
            return false;
        });
    },


    setMemberInfoDone: function () {
        Base.enable('#representative');
        RepresentativeFind.isLoadingMemberInfo = false;
    },


    setMemberInfo: function (elem) {
        if (RepresentativeFind.isLoadingMemberInfo) return;
        RepresentativeFind.isLoadingMemberInfo = true;

        pk = $(elem).attr('id');
        pk = parseInt(pk.slice(7, pk.length)); // 7 == 'member-'
        if (!pk) {
            RepresentativeFind.isLoadingMemberInfo = false;
            return;
        }

        Base.disable('#representative');
        $('.member').removeClass('member-selected');
        $(elem).addClass('member-selected');

        $.ajax(RepresentativeFind.urlMemberInfo + pk + '/', {
            success: function (data, textStatus, jqXHR) {
                $('#representative #info #data').html(data);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                var msg = '<h3>' + jqXHR.status + ' ' + errorThrown + '</h3>';
                $('#representative #info #data').html(msg);
                RepresentativeFind.setMemberInfoDone();
            }
        }).done(RepresentativeFind.setMemberInfoDone);
    },


    setupMemberInfo: function () {
        RepresentativeFind.urlMemberInfo = URL_MemberInfo.slice(0,
            URL_MemberInfo.length - 2); // slice off '0/'
        RepresentativeFind.noneSelected = $('#representative #info #data').html();
    },


    selectMemberFromLocation: function () {
        var hash = window.location.hash;
        // 8 == #member-
        var pk = parseInt(hash.slice(8, hash.length));
        if (!pk) return;

        var member = $('#representative #members #member-' + pk);
        if (!member || member.length == 0) return;

        $(member).addClass('member-selected');
        $('html, body').animate({
            // arbitrary value 100 to scroll down a bit
            scrollTop: $(member).offset().top - 100
        }, 'slow');

        RepresentativeFind.setMemberInfo($(member));
    },


    setupUnit: function () {
        $('#representative #unit-select #unit-slider').slider({
            min: 0,
            max: 2,
            change: function (event, ui) {
                if (ui.value == 0) {
                    RepresentativeFind.loadUnit('parliament');
                } else if (ui.value == 1) {
                    RepresentativeFind.loadUnit('ajara');
                } else if (ui.value == 2) {
                    RepresentativeFind.loadUnit('tbilisi');
                } // else do nothing
            }
        });
    },


    hoverIntentMembers: function () {
        var config = {
             over: function () { RepresentativeFind.setMemberInfo($(this)); },
             out: function () {},
             interval: RepresentativeFind.hoverInterval,
        };
        $('#representative #members .member').hoverIntent(config);
    },


    loadUnitDone: function () {
        RepresentativeFind.hoverIntentMembers();
        $('#representative #unit').toggle('blind');
        RepresentativeFind.selectMemberFromLocation();
        RepresentativeFind.setupFiltersParty();

        $('#representative #filter-form input').removeAttr('disabled');

        $('#representative #filter-party option').hide();
        $('#representative #filter-party .unit-all').show();
        $('#representative #filter-party .unit-' +
            RepresentativeFind.activeUnit).show();
        $('#representative #filter-party').val('all');

        Base.enable('#representative');
        RepresentativeFind.isLoadingUnit = false;
    },


    loadUnit: function (unit) {
        if (RepresentativeFind.isLoadingUnit) return;

        RepresentativeFind.isLoadingUnit = true;
        Base.disable('#representative');
        $("#representative #filter-form input").attr('disabled', 'disabled');
        $('#representative #unit').toggle('blind');
        $('#representative #unit').html('');
        $('#representative #info #data').html(RepresentativeFind.noneSelected);

        if (RepresentativeFind.unit[unit]) {
            $('#representative #unit').html(RepresentativeFind.unit[unit]);
            RepresentativeFind.activeUnit = unit;
            RepresentativeFind.loadUnitDone();
        } else {
            $.ajax(URL_Units[unit], {
                success: function(data, textStatus, jqXHR) {
                    RepresentativeFind.unit[unit] = data;
                    RepresentativeFind.activeUnit = unit;
                    $('#representative #unit').html(data);
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    var msg = '<h3>' + jqXHR.status + ' ' + errorThrown + '</h3>';
                    $('#representative #unit').html(msg);
                    RepresentativeFind.loadUnitDone();
                }
            }).done(RepresentativeFind.loadUnitDone);
        }
    },


    setup: function () {
        RepresentativeFind.setupFilters();
        RepresentativeFind.setupMemberInfo();
        RepresentativeFind.setupUnit();
        RepresentativeFind.loadUnit('parliament');
    },
};



$(function () {
    RepresentativeFind.setup();
});
