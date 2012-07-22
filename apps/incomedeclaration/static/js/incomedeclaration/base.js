/*
 * Javascript file for app incomedeclaration
 */

IncomeDeclarationBase = {
    setup: function() {
        var elem = null;
        if ($('#incomedeclaration #detail').length != 0) {
            elem = '#incomedeclaration #detail';
        }

        if (elem) {
            Base.setHeightScrollPane(
                '#incomedeclaration .body', elem, 100);
        }
    },
};

$(function () {
    IncomeDeclarationBase.setup();
});
