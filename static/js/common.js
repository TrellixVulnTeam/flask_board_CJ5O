var Common = {
    // Func: Open the modal
    OpenModal: function(){
        $("#myModal").modal();
    },
    Call_Signout: function(){
        $("#myModal").modal('hide');
        window.location.href = "Signout";
    },
    Signout: function(){
        $('#menubarHTML').hide();
        window.location.href = "/";
    },
}