$(function() {
    $('#btnLogin').click(function() {
        $.ajax({
            url: '/loginProcess',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
//                if response == "Success":
//                    window.location.href = 'Home'
//                else if response == "NotMatchPW":
//                    Alert('Does not match the Password!')
//                else if response == "NotMatchID":
//                    Alert('Does not match the ID!')
//                else if response == "Fail":
//                    Alert('Does not match ID and Password!')

                console.log(response)
                window.location.href = 'Home'
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});