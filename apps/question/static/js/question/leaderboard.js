/*
 * Javascript file for question leaderboard
 */

QuestionLeaderboard = {
    setup: function () {
        $('#question #leaderboard table').tablesorter();
    }
};


$(function () {
    QuestionLeaderboard.setup();
});
