$(document).ready(function (){
    window.resizeTo(500, 500);
    window.focus();
    $("#app").css({ "opacity":"1", "transform": "unset" });
    $("footer").css({ "opacity":"1" });
    $("body").css({ "overflow": "unset" });
    document.body.style.zoom = "100%";
});

function getpass() {
    var pass = $('#enc-pass-input').val();
    var passConfirmation = $('#enc-pass-input-confirmation').val();
    console.log(pass.replace(/^\s+|\s+$/g, ''));
    if (pass == passConfirmation){
        // passwords match
        console.log(document.getElementById('enc-pass-input').value);
        $('#enc-pass-btn').prop('disabled', false).removeClass('disabled').html('Encrypt!');
    }
    else{
        // passwords do not match
        $('#enc-pass-btn').prop('disabled', true).addClass('disabled').html('Enter matching passwords to proceed.');
    }
}

function enc() {
    console.log("start encryption")
    // call python function to open a file dialog and get the filepath here
    showPopup("enc-pass")
    passInterval = setInterval(getpass, 50);
}

function dec() {
    console.log("start decryption")
    // call python function to open a file dialog and get the filepath here
    showPopup("dec-pass")
}

function removePopups(){
    // hide all pop-ups and the overlay
    $('#overlay').prop('hidden', true);
    $('.popup').prop('hidden', true);
}

function showPopup(id){
    // remove all pre-existing popups since they might overlap
    removePopups();
    // remove hidden attribute from the popup with the specified id
    $('#overlay').prop('hidden', false);
    $('#'+id).prop('hidden', false);
}