$(function(){
    $('#btnMail').click(function(){
        $.ajax({
            url: '/sendMail',
            type: 'POST',
            success: function(response){
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});