encryptedFiletype = ".aes"

$(document).ready(function (){
    window.resizeTo(500, 520);
    window.focus();
    $("#app").css({ "opacity":"1", "transform": "unset" });
    $("footer").css({ "opacity":"1" });
    $("body").css({ "overflow": "unset" });
    document.body.style.zoom = "100%";
});

$('#dec-btn-real').prop('accept', encryptedFiletype);

document.getElementById("enc-btn").addEventListener("click", function() {
    document.getElementById("enc-btn-real").click();
});
document.getElementById("dec-btn").addEventListener("click", function() {
    document.getElementById("dec-btn-real").click();
});

document.getElementById('enc-btn-real').onchange = function () {
    alert('Selected file: ' + this.value);
  };