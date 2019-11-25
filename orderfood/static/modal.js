$(document).ready(function() {
    $('#yes').click(function() {
        callApi('yes');
    });

    $('#no').click(function() {
        callApi('no');
    });
});

function callApi(path) {
    $.ajax({
        url: '/minder/' + path
    });
}
