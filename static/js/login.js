$(function() {
    $('#btnLogin').click(function() {
        $.ajax({
            url: '/loginProcess',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                res = JSON.parse(response);
                if(res['is_success']){
                    console.log('Login IP: ', res['ip']);
                    location.replace('Home');
                }else{
                    alert('Fail to Login!')
                }
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
    $('#inputPassword').keypress(function (e) {
        var key_ENTER = 13;
        if (e.keyCode == key_ENTER) {
            $('#btnLogin').trigger('click');
        }
    });
});