$(document).ready(function() {
    console.log('here');
    $('#yes').click(function() {
        callApi('yes');
    });

    $('#no').click(function() {
        callApi('no');
    });
});

function callApi(path) {
    $.ajax({
        url: 'https://orderfood.imarsh.tech/' + path
    });
}
