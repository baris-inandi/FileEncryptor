$(document).ready(function (){
    window.resizeTo(500, 520);
    window.focus();
    $("#app").css({ "opacity":"1", "transform": "unset" });
    $("footer").css({ "opacity":"1" });
    $("body").css({ "overflow": "unset" });
    document.body.style.zoom = "100%";
});

function py(){
    eel.hello()
}