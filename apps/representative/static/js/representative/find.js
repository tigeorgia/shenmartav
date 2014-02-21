/*
 * Javascript file for app representative find
 */

RepresentativeFind = {
    isLoadingInfo: false,
    isLoadingUnit: false,
    empty: '/static/img/empty.png',
    unit: {
        'parliament': null,
        'ajara': null,
        'tbilisi': null
    },
    activeUnit: null,
    noneSelected: '',
    urlInfo: null,
    showOfferFulltextSearch: false,
    inputDelay: 2000,
    inputTime: 0,
    reallySubmitSearch: false,
    hoverInterval: 300,
    heightUnit: 70, // in %


    filterElectionType: function (type) {
            $('#filter-text').val('');
            $('#filter-party').val('all');

            if (type == 2) {
                $('.member.majoritarian').show();
                $('.member.partylist').hide();
            } else if (type == 1) {
                $('.member.partylist').show();
                $('.member.majoritarian').hide();
            } else {
                $('.member.majoritarian').show();
                $('.member.partylist').show();
            }
    },


    filterInput: function () {
        $('#filter-electiontype').val('0');
        $('#filter-party').val('all');

        var data = $('#filter-text').val().toLowerCase();
        var members = $('.member');
        members.hide();
        members.each(function() {
        	
    		var namesplit = $(this).html().toLowerCase().split("a title=\"");
    		var namesplit2 = namesplit[1].split("\" href");
    		var namesplit3 = trimNames(namesplit2[0]).split(" ");
    		
    		var firstname = namesplit3[0];
    		var lastname = namesplit3[1];
    		var fullname = firstname+" "+lastname;
    		    	
            if ($(this).hasClass('party-' + data) ||
                firstname.indexOf(data) == 0 ||
                lastname.indexOf(data) == 0 ||
                fullname.indexOf(data) == 0) {
                $(this).show();
                // don't break out: show more results
            }
        });

        if ($('.member:visible').length == 0 ||
            RepresentativeFind.showOfferFulltextSearch) {
            $('#offer-fulltext-search').show();
        } else {
            $('#offer-fulltext-search').hide();
        }
    },


    setupFiltersParty: function () {
        $('#filter-party').change(function() {
            $('#filter-text').val('');
            $('#filter-electiontype').val('0');
            var val = $(this).val();
            if (val == 'all') {
                $('.member').show();
            } else {
                $('member').hide();
                $('.member.' + val).show();
            }
        });
    },


    checkInput: function () {
        var threshold = new Date().getTime()- RepresentativeFind.inputDelay;
        if (threshold >= RepresentativeFind.inputTime) {
            $('#offer-fulltext-search').show();
        }
    },


    setupFilters: function () {
        $('#filter-electiontype').change(function () {
            RepresentativeFind.filterElectionType($(this).val());
        });

        $('#select form').submit(function() {
            if (RepresentativeFind.reallySubmitSearch) {
                return true;
            } else {
                RepresentativeFind.showOfferFulltextSearch = true;
                RepresentativeFind.filterInput($(this));
                return false;
            }
        });

        $('#filter-text').keyup(function(event) {
            if (event.which != 13) { // not enter key
                RepresentativeFind.showOfferFulltextSearch = false;
            }
            RepresentativeFind.filterInput($(this).parent());
            RepresentativeFind.inputTime = new Date().getTime();
            setTimeout(RepresentativeFind.checkInput, RepresentativeFind.inputDelay);
        });

        $('#offer-fulltext-search').click(function () {
            RepresentativeFind.reallySubmitSearch = true;
            $('#filter-submit').click();
            return false;
        });
    },


    setInfoDone: function () {
        Base.enable('#representative #info');
        RepresentativeFind.isLoadingInfo = false;
    },


    setInfo: function (elem) {
        if (RepresentativeFind.isLoadingInfo) return;
        RepresentativeFind.isLoadingInfo = true;

        pk = $(elem).attr('id');
        pk = parseInt(pk.slice(7, pk.length)); // 7 == 'member-'
        if (!pk) {
            RepresentativeFind.isLoadingInfo = false;
            return;
        }

        Base.disable('#representative #info');
        $('.member').removeClass('member-selected');
        $(elem).addClass('member-selected');

        $.ajax(RepresentativeFind.urlInfo + pk + '/', {
            success: function (data, textStatus, jqXHR) {
                $('#data').html(data);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                var msg = '<h3>' + jqXHR.status + ' ' + errorThrown + '</h3>';
                $('#data').html(msg);
                RepresentativeFind.setInfoDone();
            }
        }).done(RepresentativeFind.setInfoDone);
    },


    setupInfo: function () {
        RepresentativeFind.urlInfo = URL_Info.slice(0,
            URL_Info.length - 2); // slice off '0/'
        RepresentativeFind.noneSelected = $('#data').html();
    },


    getPKFromLocation: function () {
        var hash = window.location.hash;
        // 8 == #member-
        var pk = parseInt(hash.slice(8, hash.length));

        if (!pk) return false;
        else return pk
    },


    selectMemberFromLocation: function () {
        var pk = RepresentativeFind.getPKFromLocation();
        if (!pk) return;
        var member = $('#member-' + pk);
        if (!member || member.length == 0) return;

        $(member).addClass('member-selected');
        $('html, body').animate({
            // arbitrary value 100 to scroll down a bit
            scrollTop: $(member).offset().top - 100
        }, 'slow');

        RepresentativeFind.setInfo($(member));
    },


    setupUnit: function () {
        $('#unit-slider').slider({
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
             over: function () { RepresentativeFind.setInfo($(this)); },
             out: function () {},
             interval: RepresentativeFind.hoverInterval
        };
        $('#members .member').hoverIntent(config);
    },


    loadUnitDone: function () {
        $('#unit').toggle('blind');
        RepresentativeFind.selectMemberFromLocation();
        RepresentativeFind.setupFiltersParty();

        $('#filter-form input').removeAttr('disabled');

        var all = $('#hidden-all').html();
        var parties = $('#hidden-' + RepresentativeFind.activeUnit).html();
        $('#filter-party').html(all + parties);
        $('#filter-party').val('all');

        Base.enable('#representative #select');
        RepresentativeFind.isLoadingUnit = false;
    },


    loadUnit: function (unit) {
        if (RepresentativeFind.isLoadingUnit) return;

        RepresentativeFind.isLoadingUnit = true;
        Base.disable('#representative #select');
        $("#filter-form input").attr('disabled', 'disabled');
        $('#representative #select #unit').toggle('blind');
        $('#representative #select #unit #members').html('');
        $('#representative #info #data').html(RepresentativeFind.noneSelected);

        if (RepresentativeFind.unit[unit]) {
            $('#representative #select #unit #members').html(RepresentativeFind.unit[unit]);
            RepresentativeFind.activeUnit = unit;
            RepresentativeFind.loadUnitDone();
        } else {
            $.ajax(URL_Units[unit], {
                success: function(data, textStatus, jqXHR) {
                    RepresentativeFind.unit[unit] = data;
                    RepresentativeFind.activeUnit = unit;
                    $('#representative #select #unit #members').html(data);
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    var msg = '<h3>' + jqXHR.status + ' ' + errorThrown + '</h3>';
                    $('#representative #select #unit #members').html(msg);
                    RepresentativeFind.loadUnitDone();
                }
            }).done(RepresentativeFind.loadUnitDone);
        }
    },


    loadUnitBySlider: function (unit) {
        var elem = $('#unit-slider');
        if (unit == 'parliament') {
            elem.slider('value', 0);
        } else if (unit == 'ajara') {
            elem.slider('value', 1);
        } else if (unit == 'tbilisi') {
            elem.slider('value', 2);
        } else {
            RepresentativeFind.loadUnit('parliament');
        }
    },

    loadRightUnit: function (unit) {
        var pk = RepresentativeFind.getPKFromLocation();
        if (!pk) {
            RepresentativeFind.loadUnitBySlider(Active_Unit);
            return;
        }

        var url = URL_UnitRepresentative.slice(
            0, URL_UnitRepresentative.length - 2); // slice off '0/'

        $.ajax(url + pk + '/', {
            success: function(data, textStatus, jqXHR) {
                RepresentativeFind.loadUnitBySlider(data);
            },
            error: function (jqXHR, textStatus, errorThrown) {
                var msg = '<h3>' + jqXHR.status + ' ' + errorThrown + '</h3>';
                $('#representative #select #unit #members').html(msg);
            }
        });
    },


    setup: function () {
        RepresentativeFind.setupFilters();
        RepresentativeFind.setupInfo();
        RepresentativeFind.setupUnit();
        RepresentativeFind.loadUnit('parliament');
       // RepresentativeFind.loadRightUnit();
    }
};



$(function () {
    RepresentativeFind.setup();
});


function trimNames (str) {
    str = str.replace(/^\s+/, '');
    for (var i = str.length - 1; i >= 0; i--) {
        if (/\S/.test(str.charAt(i))) {
            str = str.substring(0, i + 1);
            break;
        }
    }
    return str;
}